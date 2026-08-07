#!/usr/bin/env bun

/*
 * Usage: bun scripts/check-static-site.js [site-directory]
 *
 * This repository is a no-build GitHub Pages site. Bun's HTMLRewriter keeps
 * the check dependency-free while validating the public shell and its docs.
 */

"use strict";

const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(process.argv[2] || process.cwd());
const rootRealpath = (() => {
  try {
    return fs.realpathSync(root);
  } catch {
    return root;
  }
})();
const failures = [];

function isInside(candidate, base) {
  return candidate === base || candidate.startsWith(`${base}${path.sep}`);
}

function decodeHtmlEntities(value) {
  return value
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">");
}

function localTarget(raw) {
  const value = decodeHtmlEntities(raw.trim());
  if (!value || value.startsWith("#") || value.startsWith("//")) return null;
  if (value.startsWith("/")) return { error: "root-relative", value };

  try {
    if (new URL(value).protocol) return null;
  } catch {
    // Relative references are expected here.
  }

  const target = value.split(/[?#]/, 1)[0];
  return target ? { target } : null;
}

function resolvedTarget(candidate, allowIndexedDirectory) {
  let stat;
  try {
    stat = fs.statSync(candidate);
  } catch {
    return null;
  }
  if (stat.isFile()) return candidate;
  if (!allowIndexedDirectory || !stat.isDirectory()) return null;

  const indexPath = path.join(candidate, "index.html");
  try {
    return fs.statSync(indexPath).isFile() ? indexPath : null;
  } catch {
    return null;
  }
}

function realpathInsideRoot(candidate) {
  try {
    return isInside(fs.realpathSync(candidate), rootRealpath);
  } catch {
    return false;
  }
}

function checkReference(sourcePath, raw, kind, allowIndexedDirectory) {
  const reference = localTarget(raw);
  if (!reference) return;
  const source = path.relative(root, sourcePath);

  if (reference.error === "root-relative") {
    failures.push(`${source} uses a root-relative Pages path: ${raw}`);
    return;
  }

  const candidate = path.resolve(path.dirname(sourcePath), reference.target);
  if (!isInside(candidate, root)) {
    failures.push(`${source} references a path outside the site: ${raw}`);
    return;
  }

  const resolved = resolvedTarget(candidate, allowIndexedDirectory);
  if (!resolved) {
    failures.push(`${source} references missing local ${kind}: ${raw}`);
    return;
  }
  if (!realpathInsideRoot(resolved)) {
    failures.push(`${source} resolves outside the site via symlink: ${raw}`);
  }
}

function checkNavigation(pageIds) {
  if (pageIds.length === 0) {
    failures.push("index.html has no data-page navigation entries");
    return;
  }

  const seen = new Set();
  for (const pageId of pageIds) {
    if (seen.has(pageId)) {
      failures.push(`index.html has duplicate navigation entry: ${pageId}`);
      continue;
    }
    seen.add(pageId);

    const filename = pageId === "index" ? "index.md" : `${pageId}.md`;
    const candidate = path.resolve(root, filename);
    if (!isInside(candidate, root)) {
      failures.push(`navigation entry '${pageId}' points outside the site`);
      continue;
    }
    const resolved = resolvedTarget(candidate, false);
    if (!resolved || !realpathInsideRoot(resolved)) {
      failures.push(`navigation entry '${pageId}' has no local ${filename}`);
    }
  }

  const indexPath = path.join(root, "index.md");
  if (!resolvedTarget(indexPath, false) || !realpathInsideRoot(indexPath)) {
    failures.push("index.md is missing; the home page cannot load");
  }
}

function checkHtml(htmlPath, source) {
  const pageIds = [];
  const rewriter = new HTMLRewriter();

  rewriter.on("[src], [href]", {
    element(element) {
      const tagName = element.tagName.toLowerCase();
      const src = element.getAttribute("src");
      const href = element.getAttribute("href");
      if (src !== null) checkReference(htmlPath, src, "asset", false);
      if (href !== null) {
        checkReference(htmlPath, href, "asset", tagName === "a" || tagName === "area");
      }
    },
  });

  rewriter.on("a[data-page]", {
    element(element) {
      const pageId = element.getAttribute("data-page")?.trim();
      if (pageId) pageIds.push(pageId);
    },
  });

  rewriter.transform(source);
  checkNavigation(pageIds);
}

function checkHtmlAssets() {
  const htmlPath = path.join(root, "index.html");
  const resolved = resolvedTarget(htmlPath, false);
  if (!resolved) {
    failures.push("index.html is missing");
    return;
  }
  if (!realpathInsideRoot(resolved)) {
    failures.push("index.html resolves outside the site via symlink");
    return;
  }

  checkHtml(htmlPath, fs.readFileSync(htmlPath, "utf8"));
}

function checkMarkdownLinks() {
  const markdownFiles = fs
    .readdirSync(root, { withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.endsWith(".md"));

  for (const entry of markdownFiles) {
    const filePath = path.join(root, entry.name);
    const source = fs.readFileSync(filePath, "utf8");
    const links = /!?\[[^\]]*\]\(\s*(?:<([^>]*)>|([^\s)]*))(?:\s+["'][^)]*["'])?\s*\)/g;
    let match;

    while ((match = links.exec(source)) !== null) {
      const rawTarget = match[1] ?? match[2];
      if (!rawTarget.trim()) {
        failures.push(`${entry.name} has an empty Markdown link target`);
        continue;
      }
      checkReference(filePath, rawTarget, "Markdown link", false);
    }
  }
}

checkHtmlAssets();
checkMarkdownLinks();

if (failures.length > 0) {
  console.error("Static site check failed:");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exitCode = 1;
} else {
  console.log("Static site check passed (local HTML assets, navigation, and Markdown links).");
}

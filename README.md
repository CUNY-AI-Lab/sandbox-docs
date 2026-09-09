# CAIL Sandbox Docs redirects

Documentation is maintained in the [CUNY AI Lab website repository](https://github.com/CUNY-AI-Lab/CUNY-AI-Lab-website/tree/main/src/content/sandbox-docs) and published at https://ailab.gc.cuny.edu/sandbox-docs/.

This former GitHub Pages site redirects old bookmarks to the matching article. Root hash links, article paths, `.html` and `.md` URLs preserve their destination; query strings and section anchors are retained. GitHub Pages serves static files, so these are browser redirects using `location.replace`, not HTTP 301 responses. A visible link and guide list work without JavaScript.

The original Markdown remains in Git as historical source and is excluded from Pages publication by `_config.yml`. The 404 page handles old article paths. Future content changes belong in the website repository.

Run `bun scripts/check-static-site.js` and `bun scripts/check-redirect.js` before publishing. Merge to main publishes through the existing GitHub Pages build.

#!/usr/bin/env python3
"""
Parse WordPress XML export and convert to HTML sections for cail-docs SPA.
"""

import xml.etree.ElementTree as ET
import html
import re
from pathlib import Path

def parse_wp_export(xml_file):
    """Parse WordPress export XML and extract published pages."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    ns = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'wp': 'http://wordpress.org/export/1.2/',
    }
    
    channel = root.find('channel')
    items = channel.findall('item')
    
    pages = []
    for item in items:
        post_type = item.find('wp:post_type', ns)
        status = item.find('wp:status', ns)
        
        if post_type is not None and status is not None:
            if post_type.text == 'page' and status.text == 'publish':
                title = item.find('title').text or '(No title)'
                slug = item.find('wp:post_name', ns).text or ''
                content_elem = item.find('content:encoded', ns)
                content = content_elem.text if content_elem is not None else ''
                
                pages.append({
                    'title': title,
                    'slug': slug,
                    'content': content
                })
    
    return sorted(pages, key=lambda p: p['title'])

def clean_wp_html(content):
    """Clean WordPress HTML and convert to cail-docs compatible HTML."""
    if not content:
        return ''
    
    # Remove inline styles
    content = re.sub(r'style="[^"]*"', '', content)
    content = re.sub(r"style='[^']*'", '', content)
    
    # Remove WordPress-specific classes
    content = re.sub(r'class="wp-[^"]*"', '', content)
    content = re.sub(r'class="alignright"', '', content)
    content = re.sub(r'class="alignleft"', '', content)
    
    # Convert WordPress expand shortcodes to details/summary
    # [expand title="Question"]Answer[/expand]
    def expand_replacer(match):
        title = match.group(1)
        return f'<details><summary>{title}</summary>'
    
    content = re.sub(r'\[expand title="([^"]+)"\]', expand_replacer, content)
    content = re.sub(r'\[/expand\]', '</details>', content)
    
    # Remove empty paragraphs
    content = re.sub(r'<p>\s*</p>', '', content)
    
    # Fix image URLs (keep them absolute)
    # Already absolute URLs to commons.gc.cuny.edu, so no changes needed
    
    return content.strip()

def generate_html_section(page):
    """Generate HTML section for a single page."""
    title = html.escape(page['title'])
    slug = page['slug']
    content = clean_wp_html(page['content'])
    
    output = f'''  <!-- {title.upper()} -->
  <div class="page" id="{slug}">
    <div class="breadcrumb"><a href="#">Docs</a> / AI Toolkit / <a href="#{slug}">{title}</a></div>
    <h1>{title}</h1>
    {content}
  </div>
'''
    return output

def generate_sidebar_links(pages):
    """Generate sidebar navigation links."""
    links = []
    for page in pages:
        title = html.escape(page['title'])
        slug = page['slug']
        links.append(f'  <a href="#{slug}" class="nav-link" data-page="{slug}">{title}</a>')
    
    return '\n'.join(links)

def main():
    xml_file = 'teachcunyaitoolkit.WordPress.2026-02-22.xml'
    
    print("Parsing WordPress export...")
    pages = parse_wp_export(xml_file)
    print(f"Found {len(pages)} pages")
    
    print("\nGenerating HTML sections...")
    sections_html = []
    for page in pages:
        section = generate_html_section(page)
        sections_html.append(section)
    
    print("\nGenerating sidebar links...")
    sidebar_links = generate_sidebar_links(pages)
    
    # Write sections to file
    output_file = 'ai_toolkit_sections.html'
    with open(output_file, 'w') as f:
        f.write('\n'.join(sections_html))
    
    print(f"\nWrote sections to {output_file}")
    
    # Write sidebar links to file
    sidebar_file = 'ai_toolkit_sidebar.html'
    with open(sidebar_file, 'w') as f:
        f.write(sidebar_links)
    
    print(f"Wrote sidebar links to {sidebar_file}")
    
    print("\nPage list:")
    for page in pages:
        print(f"  • {page['title']} ({page['slug']})")

if __name__ == '__main__':
    main()

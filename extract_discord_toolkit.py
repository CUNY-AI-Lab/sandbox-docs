#!/usr/bin/env python3
"""
Extract Discord Educational Toolkit pages to markdown format
Organized by kit: Starter Kit, Design Kit, Instructional Kit
"""

import xml.etree.ElementTree as ET
import re
import os
from pathlib import Path
from html import unescape
from html.parser import HTMLParser

class HTMLToMarkdown(HTMLParser):
    """Simple HTML to Markdown converter"""
    def __init__(self):
        super().__init__()
        self.result = []
        self.list_stack = []
        self.in_heading = False
        self.heading_level = 0
        self.in_paragraph = False
        self.in_list_item = False
        self.in_strong = False
        self.in_em = False
        self.in_link = False
        self.link_href = ''
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.in_heading = True
            self.heading_level = int(tag[1])
            self.result.append('\n' + '#' * self.heading_level + ' ')
        elif tag == 'p':
            self.in_paragraph = True
            self.result.append('\n\n')
        elif tag == 'br':
            self.result.append('  \n')
        elif tag == 'strong' or tag == 'b':
            self.in_strong = True
            self.result.append('**')
        elif tag == 'em' or tag == 'i':
            self.in_em = True
            self.result.append('*')
        elif tag == 'a':
            self.in_link = True
            self.link_href = attrs_dict.get('href', '')
            self.result.append('[')
        elif tag == 'img':
            src = attrs_dict.get('src', '')
            alt = attrs_dict.get('alt', 'image')
            self.result.append(f'\n\n![{alt}]({src})\n\n')
        elif tag == 'ul':
            self.list_stack.append('ul')
            self.result.append('\n')
        elif tag == 'ol':
            self.list_stack.append('ol')
            self.result.append('\n')
        elif tag == 'li':
            self.in_list_item = True
            indent = '  ' * (len(self.list_stack) - 1)
            if self.list_stack and self.list_stack[-1] == 'ul':
                self.result.append(f'{indent}- ')
            else:
                self.result.append(f'{indent}1. ')
        elif tag == 'blockquote':
            self.result.append('\n> ')
        elif tag == 'code':
            self.result.append('`')
        elif tag == 'pre':
            self.result.append('\n```\n')
            
    def handle_endtag(self, tag):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.in_heading = False
            self.result.append('\n')
        elif tag == 'p':
            self.in_paragraph = False
        elif tag == 'strong' or tag == 'b':
            self.in_strong = False
            self.result.append('**')
        elif tag == 'em' or tag == 'i':
            self.in_em = False
            self.result.append('*')
        elif tag == 'a':
            self.in_link = False
            self.result.append(f']({self.link_href})')
        elif tag == 'ul' or tag == 'ol':
            if self.list_stack:
                self.list_stack.pop()
            self.result.append('\n')
        elif tag == 'li':
            self.in_list_item = False
            self.result.append('\n')
        elif tag == 'code':
            self.result.append('`')
        elif tag == 'pre':
            self.result.append('\n```\n')
            
    def handle_data(self, data):
        # Clean up whitespace but preserve structure
        if self.in_heading or self.in_link:
            self.result.append(data.strip())
        else:
            self.result.append(data)
            
    def get_markdown(self):
        md = ''.join(self.result)
        # Clean up excessive newlines
        md = re.sub(r'\n{3,}', '\n\n', md)
        return md.strip()

# Parse WordPress XML
tree = ET.parse('discordeducationaltoolkit.WordPress.2026-02-22.xml')
root = tree.getroot()

# Namespaces
ns = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

# Output directories
output_base = Path('discord-toolkit-md')
output_base.mkdir(exist_ok=True)

# Kit directories
kits = {
    'starter-kit': output_base / 'starter-kit',
    'design-kit': output_base / 'design-kit', 
    'instructional-kit': output_base / 'instructional-kit',
    'other': output_base / 'other'
}

for kit_dir in kits.values():
    kit_dir.mkdir(exist_ok=True)

# Extract all pages
items = root.findall('.//item')
pages = []

for item in items:
    post_type = item.find('wp:post_type', ns)
    if post_type is not None and post_type.text == 'page':
        title_elem = item.find('title')
        link_elem = item.find('link')
        content_elem = item.find('content:encoded', ns)
        excerpt_elem = item.find('excerpt:encoded', ns)
        creator_elem = item.find('dc:creator', ns)
        status_elem = item.find('wp:status', ns)
        
        title = title_elem.text if title_elem is not None else 'Untitled'
        link = link_elem.text if link_elem is not None else ''
        content = content_elem.text if content_elem is not None else ''
        excerpt = excerpt_elem.text if excerpt_elem is not None else ''
        creator = creator_elem.text if creator_elem is not None else ''
        status = status_elem.text if status_elem is not None else ''
        
        # Skip drafts and private pages
        if status != 'publish':
            continue
            
        pages.append({
            'title': title,
            'link': link,
            'content': content,
            'excerpt': excerpt,
            'creator': creator
        })

# Categorize pages by kit based on URL path
def categorize_page(link):
    """Determine which kit a page belongs to based on URL"""
    link_lower = link.lower()
    
    # Starter Kit pages
    starter_keywords = ['server-setup', 'student-onboarding', 'starter-kit']
    
    # Design Kit pages  
    design_keywords = ['server-design', 'design-kit', 'server-customization', 
                       'role-permissions', 'role-management', 'server-models']
    
    # Instructional Kit pages
    instructional_keywords = ['course-design', 'course-announcements', 
                             'class-discussion', 'group-collaboration',
                             'course-templates', 'template-collection']
    
    for keyword in starter_keywords:
        if keyword in link_lower:
            return 'starter-kit'
    
    for keyword in design_keywords:
        if keyword in link_lower:
            return 'design-kit'
            
    for keyword in instructional_keywords:
        if keyword in link_lower:
            return 'instructional-kit'
    
    return 'other'

# Process and save pages
print(f"Processing {len(pages)} pages...\n")

for page in pages:
    title = page['title']
    link = page['link']
    content_html = page['content']
    
    # Determine kit category
    kit = categorize_page(link)
    
    # Convert HTML to Markdown
    parser = HTMLToMarkdown()
    if content_html:
        parser.feed(unescape(content_html))
        content_md = parser.get_markdown()
    else:
        content_md = ''
    
    # Create filename from title
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    filename = re.sub(r'[-\s]+', '-', filename)
    filename = f"{filename}.md"
    
    # Build markdown document
    md_content = f"""# {title}

**Source:** {link}  
**Author:** {page['creator']}

---

{content_md}
"""
    
    # Write to file
    output_path = kits[kit] / filename
    output_path.write_text(md_content, encoding='utf-8')
    
    print(f"[{kit:20s}] {title}")

print(f"\n✅ Extraction complete!")
print(f"📁 Output: {output_base.absolute()}")
print(f"\nKit breakdown:")
for kit_name, kit_path in kits.items():
    count = len(list(kit_path.glob('*.md')))
    print(f"  {kit_name:20s}: {count} pages")

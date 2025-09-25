# QRTick Blog

A static blog generator for QRTick documentation and updates, built with Python and designed to match the QRTick brand styling.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate the blog:**
   ```bash
   python blog_generator.py
   ```

3. **View the results:**
   Open `blog_html/index.html` in your browser to see the generated blog.

## Blog Post Structure

### YAML Frontmatter

Each blog post should start with YAML frontmatter containing metadata:

```yaml
---
title: "Your Blog Post Title"
date: "2025-01-15"  # YYYY-MM-DD format preferred
author: "Author Name"
excerpt: "A brief description that appears on the blog index and in meta tags."
tags:
  - "tag1"
  - "tag2"
  - "tag3"
---
```

### Markdown Content

After the frontmatter, write your content in standard Markdown:

```markdown
# Your Main Heading

Regular paragraph text with **bold** and *italic* formatting.

## Section Headings

- Bullet points
- More bullet points

### Subsections

> Blockquotes for important information

`Code snippets` and code blocks are supported.
```

## File Organization

```
qrtick-blog/
├── blog/                    # Source markdown files
│   ├── sample_post.md
│   └── qrtick_updates_june_2025.md
├── blog_html/              # Generated HTML files (created automatically)
│   ├── index.html          # Blog index page
│   └── *.html              # Individual blog posts
├── blog_generator.py       # Main generator script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Features

### Automatic Generation
- **Blog index page** with all posts listed chronologically
- **Individual post pages** with consistent styling
- **Responsive design** that works on all devices
- **SEO-friendly** with proper meta tags

### Styling
- **QRTick brand colors** and typography
- **Professional layout** matching the main docs site
- **Tag support** for categorizing posts
- **Author attribution** and publication dates

### Content Features
- **YAML frontmatter** for structured metadata
- **Markdown support** with extensions for tables, code highlighting, and more
- **Automatic excerpts** if not provided in frontmatter
- **Tag-based organization** for easy content discovery

## Adding New Blog Posts

1. **Create a new markdown file** in the `blog/` directory
2. **Add YAML frontmatter** with title, date, author, excerpt, and tags
3. **Write your content** in Markdown below the frontmatter
4. **Run the generator** with `python blog_generator.py`
5. **Check the output** in `blog_html/`

### Example New Post

Create `blog/my-new-post.md`:

```markdown
---
title: "Tips for Successful Fundraising Events"
date: "2025-01-20"
author: "Sarah Johnson"
excerpt: "Learn proven strategies for maximizing donations and attendance at your fundraising events."
tags:
  - "fundraising"
  - "event-tips"
  - "best-practices"
---

# Tips for Successful Fundraising Events

Your content goes here...
```

## Dependencies

- **Python 3.7+**
- **markdown**: For converting Markdown to HTML
- **PyYAML**: For parsing YAML frontmatter

Install with: `pip install -r requirements.txt`

## Command Line Usage

```bash
# Generate all blog posts
python blog_generator.py

# The script will:
# 1. Scan the blog/ directory for .md files
# 2. Parse YAML frontmatter and Markdown content
# 3. Generate HTML files in blog_html/
# 4. Create an index page listing all posts
```

---

*QRTick Blog Generator - Making content creation as easy as event management*

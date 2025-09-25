# QRTick Blog Structure Reference

## YAML Frontmatter Template

```yaml
---
title: "Your Blog Post Title"
date: "2025-01-15"  # YYYY-MM-DD format preferred
author: "Author Name"
excerpt: "Brief description for the blog index and SEO meta tags."
tags:
  - "tag1"
  - "tag2"
  - "tag3"
---
```

## Required Files Structure

```
qrtick-blog/
├── blog/                                   # Source markdown files
│   ├── sample_post.md                      # Example welcome post
│   ├── qrtick_updates_june_2025.md         # Platform updates post
│   └── [your-new-posts].md                # Your new blog posts
├── blog_html/                              # Generated HTML (auto-created)
│   ├── index.html                          # Blog index page
│   └── [generated-post-slugs].html         # Individual post pages
├── blog_generator.py                       # Main generator script
├── requirements.txt                        # Python dependencies
├── README.md                              # Full documentation
└── BLOG_STRUCTURE.md                     # This reference file
```

## Quick Commands

**Generate Blog:**
```bash
python blog_generator.py
```

**Install Dependencies:**
```bash
pip install -r requirements.txt
```

**View Blog:**
Open `blog_html/index.html` in your browser

## YAML Frontmatter Fields

- **title**: Post title (appears in `<title>` and heading)
- **date**: Publication date (used for sorting)
- **author**: Author name (appears in byline)
- **excerpt**: Brief description (appears in index and meta description)
- **tags**: List of tags for categorization

## File Naming

- Use `.md` extension for blog posts
- Files can have any name - the URL slug is generated from the title
- Date in filename is optional - use YAML frontmatter date instead

## Generated HTML Features

- ✅ Responsive design with QRTick branding
- ✅ SEO-friendly meta tags
- ✅ Author attribution and dates
- ✅ Tag-based categorization
- ✅ Blog index with excerpts
- ✅ Navigation between posts and index
- ✅ Professional styling matching QRTick docs 
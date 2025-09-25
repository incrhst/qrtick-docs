#!/usr/bin/env python3
"""
QRTick Blog Generator

This script reads markdown files from the blog folder and generates:
1. Individual HTML blog post pages
2. A blog index page listing all entries
3. Consistent styling matching the QRTick docs design

Blog posts should include YAML frontmatter with:
- title: Blog post title
- date: Publication date (YYYY-MM-DD or readable format)
- author: Author name
- excerpt: Optional excerpt (if not provided, auto-generated)
- tags: Optional list of tags
"""

import os
import re
import yaml
import markdown
from datetime import datetime
from pathlib import Path

class BlogGenerator:
    def __init__(self, blog_dir="blog", output_dir="blog_html"):
        self.blog_dir = Path(blog_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # QRTick brand colors and styling
        self.template_vars = {
            'bg_color': '#FFF9EA',
            'header_bg': '#3D3939',
            'accent_color': '#FDC230',
            'text_color': '#3D3939',
            'card_bg': '#fff'
        }
    
    def get_html_template(self):
        """Base HTML template matching QRTick docs styling"""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - QRTick Blog</title>
    <meta name="description" content="{excerpt}">
    <meta name="author" content="{author}">
    <link rel="icon" type="image/png" sizes="32x32" href="../icon-32x32.png">
    <link rel="icon" type="image/png" sizes="192x192" href="../icon-192x192.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../icon-180x180.png">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: 'Inter', 'Roboto', Arial, sans-serif;
            background: #FFF9EA;
            color: #3D3939;
            line-height: 1.6;
        }}
        .header {{
            padding: 2rem 1rem 1rem 1rem;
            text-align: center;
            background-color: #3D3939;
            box-shadow: 0 2px 8px rgba(61, 57, 57, 0.1);
        }}
        .logo {{
            max-width: 180px;
            height: auto;
            margin-bottom: 0.5rem;
        }}
        .nav-links {{
            margin-top: 1rem;
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
        }}
        .nav-link {{
            color: #FDC230;
            text-decoration: none;
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            transition: background-color 0.2s;
        }}
        .nav-link:hover {{
            background-color: rgba(253, 194, 48, 0.1);
            text-decoration: underline;
        }}
        .container {{
            max-width: 800px;
            margin: 2rem auto 0 auto;
            padding: 2rem;
            background: #fff;
            border-radius: 16px;
            box-shadow: 0 2px 12px rgba(61, 57, 57, 0.07);
        }}
        .blog-meta {{
            background: #EEEEEE;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            font-size: 0.9rem;
            border-left: 4px solid #FDC230;
        }}
        .blog-meta .author {{
            font-weight: 600;
            color: #3D3939;
        }}
        .blog-tags {{
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid #EEEEEE;
        }}
        .tag {{
            display: inline-block;
            background: #FDC230;
            color: #3D3939;
            padding: 0.25rem 0.75rem;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }}
        .blog-content h1 {{
            color: #3D3939;
            font-weight: 700;
            letter-spacing: -0.5px;
            margin-bottom: 0.5rem;
        }}
        .blog-content h2 {{
            color: #3D3939;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #FDC230;
            padding-bottom: 0.5rem;
        }}
        .blog-content h3 {{
            color: #3D3939;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }}
        .blog-content p {{
            margin-bottom: 1rem;
        }}
        .blog-content ul, .blog-content ol {{
            margin: 1rem 0;
            padding-left: 2rem;
        }}
        .blog-content li {{
            margin-bottom: 0.5rem;
        }}
        .blog-content blockquote {{
            border-left: 4px solid #FDC230;
            margin: 1.5rem 0;
            padding-left: 1.5rem;
            font-style: italic;
            background: #FFF9EA;
            padding: 1rem 1rem 1rem 2rem;
            border-radius: 0 8px 8px 0;
        }}
        .blog-content code {{
            background: #f4f4f4;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
        }}
        .blog-content pre {{
            background: #f4f4f4;
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
        }}
        .blog-content pre code {{
            background: none;
            padding: 0;
        }}
        .footer {{
            margin-top: 3rem;
            padding: 2rem 1rem 1rem 1rem;
            background: #3D3939;
            text-align: center;
            color: #EEEEEE;
            font-size: 1rem;
        }}
        .footer-logo {{
            max-width: 120px;
            margin-bottom: 0.5rem;
        }}
        .footer-link {{
            color: #FDC230;
            text-decoration: none;
            font-weight: 600;
        }}
        .footer-link:hover {{
            text-decoration: underline;
        }}
        .back-to-blog {{
            display: inline-block;
            background-color: #FDC230;
            color: #3D3939;
            padding: 0.75rem 1.5rem;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            margin-bottom: 2rem;
            transition: background-color 0.2s;
        }}
        .back-to-blog:hover {{
            background-color: #e5af2b;
        }}
    </style>
</head>
<body>
    <header class="header">
        <a href="https://qrtick.com" target="_blank" rel="noopener noreferrer">
            <img src="../qrtick-logo-alt.svg" alt="QRTick Logo" class="logo">
        </a>
        <div class="nav-links">
            <a href="../index.html" class="nav-link">Docs Home</a>
            <a href="index.html" class="nav-link">Blog</a>
            <a href="https://qrtick.com" class="nav-link" target="_blank" rel="noopener noreferrer">QRTick.com →</a>
        </div>
    </header>
    <main class="container">
        {content}
    </main>
    <footer class="footer">
        <img src="../qrtick-logo-alt.svg" alt="QRTick Logo" class="footer-logo">
        <p>&copy; 2025 QRTick. Making events easier to manage and more profitable.</p>
        <p><a href="https://qrtick.com" class="footer-link" target="_blank" rel="noopener noreferrer">Visit QRTick.com</a></p>
    </footer>
</body>
</html>"""

    def get_blog_index_template(self):
        """Template for the blog index page"""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QRTick Blog - Latest Updates and Insights</title>
    <meta name="description" content="Latest updates, insights, and tips for successful event management in Jamaica from the QRTick team.">
    <link rel="icon" type="image/png" sizes="32x32" href="../icon-32x32.png">
    <link rel="icon" type="image/png" sizes="192x192" href="../icon-192x192.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../icon-180x180.png">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: 'Inter', 'Roboto', Arial, sans-serif;
            background: #FFF9EA;
            color: #3D3939;
        }}
        .header {{
            padding: 2rem 1rem 1rem 1rem;
            text-align: center;
            background-color: #3D3939;
            box-shadow: 0 2px 8px rgba(61, 57, 57, 0.1);
        }}
        .logo {{
            max-width: 180px;
            height: auto;
            margin-bottom: 0.5rem;
        }}
        .nav-links {{
            margin-top: 1rem;
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
        }}
        .nav-link {{
            color: #FDC230;
            text-decoration: none;
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            transition: background-color 0.2s;
        }}
        .nav-link:hover {{
            background-color: rgba(253, 194, 48, 0.1);
            text-decoration: underline;
        }}
        .container {{
            max-width: 800px;
            margin: 2rem auto 0 auto;
            padding: 2rem;
            background: #fff;
            border-radius: 16px;
            box-shadow: 0 2px 12px rgba(61, 57, 57, 0.07);
        }}
        .blog-post {{
            background: #FFF9EA;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 1px 4px rgba(61, 57, 57, 0.04);
            border-left: 4px solid #FDC230;
        }}
        .blog-post h2 {{
            margin-top: 0;
            margin-bottom: 0.5rem;
            color: #3D3939;
        }}
        .blog-post h2 a {{
            color: #3D3939;
            text-decoration: none;
        }}
        .blog-post h2 a:hover {{
            color: #1A73E8;
            text-decoration: underline;
        }}
        .blog-meta {{
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 1rem;
        }}
        .blog-author {{
            font-weight: 600;
            color: #3D3939;
        }}
        .blog-excerpt {{
            margin-bottom: 1rem;
            line-height: 1.6;
        }}
        .blog-tags {{
            margin-bottom: 1rem;
        }}
        .tag {{
            display: inline-block;
            background: #FDC230;
            color: #3D3939;
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: 600;
            margin-right: 0.3rem;
            margin-bottom: 0.3rem;
        }}
        .read-more {{
            display: inline-block;
            background-color: #FDC230;
            color: #3D3939;
            padding: 0.5rem 1rem;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.9rem;
            transition: background-color 0.2s;
        }}
        .read-more:hover {{
            background-color: #e5af2b;
        }}
        .footer {{
            margin-top: 3rem;
            padding: 2rem 1rem 1rem 1rem;
            background: #3D3939;
            text-align: center;
            color: #EEEEEE;
            font-size: 1rem;
        }}
        .footer-logo {{
            max-width: 120px;
            margin-bottom: 0.5rem;
        }}
        .footer-link {{
            color: #FDC230;
            text-decoration: none;
            font-weight: 600;
        }}
        .footer-link:hover {{
            text-decoration: underline;
        }}
        h1 {{
            color: #3D3939;
            font-weight: 700;
            letter-spacing: -0.5px;
            text-align: center;
            margin-bottom: 2rem;
        }}
    </style>
</head>
<body>
    <header class="header">
        <a href="https://qrtick.com" target="_blank" rel="noopener noreferrer">
            <img src="../qrtick-logo-alt.svg" alt="QRTick Logo" class="logo">
        </a>
        <div class="nav-links">
            <a href="../index.html" class="nav-link">Docs Home</a>
            <a href="index.html" class="nav-link">Blog</a>
            <a href="https://qrtick.com" class="nav-link" target="_blank" rel="noopener noreferrer">QRTick.com →</a>
        </div>
    </header>
    <main class="container">
        <h1>QRTick Blog</h1>
        <p style="text-align: center; margin-bottom: 3rem; font-size: 1.1rem;">Latest updates, insights, and tips for successful event management in Jamaica.</p>
        {blog_posts}
    </main>
    <footer class="footer">
        <img src="../qrtick-logo-alt.svg" alt="QRTick Logo" class="footer-logo">
        <p>&copy; 2025 QRTick. Making events easier to manage and more profitable.</p>
        <p><a href="https://qrtick.com" class="footer-link" target="_blank" rel="noopener noreferrer">Visit QRTick.com</a></p>
    </footer>
</body>
</html>"""

    def parse_frontmatter(self, content):
        """Parse YAML frontmatter from markdown content"""
        if not content.startswith('---'):
            return {}, content
        
        try:
            # Split the content at the second '---'
            parts = content.split('---', 2)
            if len(parts) < 3:
                return {}, content
            
            frontmatter = yaml.safe_load(parts[1])
            markdown_content = parts[2].strip()
            
            return frontmatter or {}, markdown_content
        except yaml.YAMLError as e:
            print(f"Error parsing YAML frontmatter: {e}")
            return {}, content

    def extract_metadata(self, content, frontmatter):
        """Extract or generate metadata from frontmatter and content"""
        # Use frontmatter data with fallbacks
        title = frontmatter.get('title', self._extract_title_from_content(content))
        date = self._parse_date(frontmatter.get('date', datetime.now().strftime("%B %d, %Y")))
        author = frontmatter.get('author', 'QRTick Team')
        excerpt = frontmatter.get('excerpt') or self._generate_excerpt(content)
        tags = frontmatter.get('tags', [])
        
        return title, date, author, excerpt, tags

    def _extract_title_from_content(self, content):
        """Extract title from first # heading in content"""
        lines = content.strip().split('\n')
        for line in lines:
            if line.strip().startswith('# '):
                return line.strip()[2:].strip()
        return "Blog Post"

    def _parse_date(self, date_input):
        """Parse date from various formats"""
        if isinstance(date_input, str):
            # Try common date patterns
            date_patterns = [
                ('%Y-%m-%d', None),  # "2025-06-15"
                ('%B %d, %Y', None),  # "June 15, 2025"
                ('%B %Y', None),  # "June 2025"
            ]
            
            for pattern, _ in date_patterns:
                try:
                    parsed_date = datetime.strptime(date_input, pattern)
                    return parsed_date.strftime("%B %d, %Y")
                except ValueError:
                    continue
            
            return date_input  # Return as-is if no pattern matches
        elif hasattr(date_input, 'strftime'):
            return date_input.strftime("%B %d, %Y")
        else:
            return str(date_input)

    def _generate_excerpt(self, content):
        """Generate excerpt from content"""
        lines = content.strip().split('\n')
        content_lines = []
        in_content = False
        
        for line in lines:
            if line.strip().startswith('#'):
                in_content = True
                continue
            if in_content and line.strip() and not line.strip().startswith('*'):
                content_lines.append(line.strip())
                if len(' '.join(content_lines)) > 200:
                    break
        
        if content_lines:
            excerpt = ' '.join(content_lines)[:300]
            if len(excerpt) == 300:
                excerpt = excerpt.rsplit(' ', 1)[0] + "..."
            return excerpt
        
        return "Read this blog post for the latest QRTick updates and insights."

    def markdown_to_html(self, markdown_content):
        """Convert markdown to HTML"""
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
        return md.convert(markdown_content)

    def generate_blog_post(self, markdown_file):
        """Generate individual blog post HTML"""
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, markdown_content = self.parse_frontmatter(content)
        title, date, author, excerpt, tags = self.extract_metadata(markdown_content, frontmatter)
        html_content = self.markdown_to_html(markdown_content)
        
        # Create tags HTML
        tags_html = ""
        if tags:
            tags_html = '<div class="blog-tags">' + ''.join([f'<span class="tag">{tag}</span>' for tag in tags]) + '</div>'
        
        # Create blog meta section
        meta_html = f"""
        <a href="index.html" class="back-to-blog">← Back to Blog</a>
        <div class="blog-meta">
            <strong>Published:</strong> {date} • <span class="author">By {author}</span>
        </div>
        <div class="blog-content">
            {html_content}
        </div>
        {tags_html}
        """
        
        # Generate full HTML
        full_html = self.get_html_template().format(
            title=title,
            excerpt=excerpt[:160] if len(excerpt) > 160 else excerpt,  # Meta description
            author=author,
            content=meta_html
        )
        
        # Create output filename
        slug = re.sub(r'[^a-zA-Z0-9\-_]', '-', title.lower())
        slug = re.sub(r'-+', '-', slug).strip('-')
        output_file = self.output_dir / f"{slug}.html"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        return {
            'title': title,
            'date': date,
            'author': author,
            'excerpt': excerpt,
            'tags': tags,
            'filename': output_file.name,
            'slug': slug
        }

    def generate_blog_index(self, posts):
        """Generate blog index page"""
        blog_posts_html = ""
        
        # Sort posts by date (newest first)
        sorted_posts = sorted(posts, key=lambda x: x['date'], reverse=True)
        
        for post in sorted_posts:
            # Create tags HTML for index
            tags_html = ""
            if post['tags']:
                tags_html = '<div class="blog-tags">' + ''.join([f'<span class="tag">{tag}</span>' for tag in post['tags']]) + '</div>'
            
            blog_posts_html += f"""
            <article class="blog-post">
                <h2><a href="{post['filename']}">{post['title']}</a></h2>
                <div class="blog-meta">{post['date']} • <span class="blog-author">By {post['author']}</span></div>
                {tags_html}
                <div class="blog-excerpt">{post['excerpt']}</div>
                <a href="{post['filename']}" class="read-more">Read More →</a>
            </article>
            """
        
        full_html = self.get_blog_index_template().format(
            blog_posts=blog_posts_html
        )
        
        index_file = self.output_dir / "index.html"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f"Generated blog index: {index_file}")

    def generate_all(self):
        """Generate all blog posts and index"""
        if not self.blog_dir.exists():
            print(f"Blog directory '{self.blog_dir}' not found!")
            return
        
        posts = []
        markdown_files = list(self.blog_dir.glob("*.md"))
        
        if not markdown_files:
            print(f"No markdown files found in '{self.blog_dir}'")
            return
        
        print(f"Found {len(markdown_files)} markdown files")
        
        for md_file in markdown_files:
            print(f"Processing: {md_file.name}")
            try:
                post_data = self.generate_blog_post(md_file)
                posts.append(post_data)
                print(f"Generated: {post_data['filename']}")
            except Exception as e:
                print(f"Error processing {md_file.name}: {e}")
        
        if posts:
            self.generate_blog_index(posts)
            print(f"\nGenerated {len(posts)} blog posts")
            print(f"Blog available at: {self.output_dir}/index.html")
        else:
            print("No blog posts were generated")

def main():
    """Main function to run the blog generator"""
    import sys
    
    # Check if required libraries are available
    try:
        import markdown
        import yaml
    except ImportError as e:
        print(f"Error: Required library not found: {e}")
        print("Install dependencies with: pip install -r requirements.txt")
        sys.exit(1)
    
    generator = BlogGenerator()
    generator.generate_all()

if __name__ == "__main__":
    main() 
import os
import glob

html_files = glob.glob('/Users/davidbain/difiledem/Downloads/code/qrtick-docs/*.html')

search_str = """            <button id="menu-btn" class="menu-btn" aria-label="Open menu">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
            </button>
        </div>"""

replace_str = """            <div style="display: flex; align-items: center;">
                <a href="https://qrtick.com" style="color: #FFF9EA; text-decoration: none; font-size: 0.9rem; opacity: 0.8; transition: opacity 0.2s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.8'">Buy Tickets</a>
                <button id="menu-btn" class="menu-btn" aria-label="Open menu">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                </button>
            </div>
        </div>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_str in content:
        new_content = content.replace(search_str, replace_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Skipped {file} - structure not found")

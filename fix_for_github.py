import os
import shutil
import re

src_html = r"c:\Users\vicki\OneDrive\문서\antigravity\index.html"
src_css = r"c:\Users\vicki\OneDrive\문서\antigravity\styles.css"
output_dir = r"c:\Users\vicki\OneDrive\문서\뉴포트폴리오"

# Create images directory
images_dir = os.path.join(output_dir, "images")
os.makedirs(images_dir, exist_ok=True)

# Copy css
shutil.copy2(src_css, os.path.join(output_dir, "styles.css"))

# Read HTML
with open(src_html, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find all file:/// image paths
pattern = r'src="file:///(C:/Users/[^"]+)"'
matches = re.finditer(pattern, html_content)

for match in matches:
    full_path = match.group(1)
    local_path = full_path.replace('/', '\\')
    
    filename = os.path.basename(local_path)
    
    if os.path.exists(local_path):
        shutil.copy2(local_path, os.path.join(images_dir, filename))
        print(f"Copied {filename}")
    else:
        print(f"File not found: {local_path}")
        
    html_content = html_content.replace(match.group(0), f'src="images/{filename}"')

# Write updated HTML
with open(os.path.join(output_dir, "index.html"), 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Done. Check the new files in the 뉴포트폴리오 folder.")

import os
import shutil

src_dir = r"C:\Users\vicki\.gemini\antigravity\brain\4bf980be-a0d3-4f3c-90b7-9f4178421185"
dst_dir = r"c:\Users\vicki\OneDrive\문서\antigravity\assets"

os.makedirs(dst_dir, exist_ok=True)

for f in os.listdir(src_dir):
    if f.startswith("media__"):
        src = os.path.join(src_dir, f)
        dst = os.path.join(dst_dir, f)
        shutil.copy2(src, dst)
        print(f"Copied {f}")

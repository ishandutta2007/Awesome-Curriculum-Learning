import os
import re

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Emojis and Banner
banner_svg = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#grad1)" />
  <text x="50%" y="50%" font-size="48" fill="white" font-family="Arial" dominant-baseline="middle" text-anchor="middle">Awesome Curriculum Learning</text>
  <circle cx="50" cy="50" r="40" fill="rgba(255,255,255,0.5)">
    <animate attributeName="r" values="40;60;40" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(banner_svg)

content = content.replace("# Awesome-Curriculum-Learning", "# 🚀 Awesome-Curriculum-Learning 🚀\\n\\n![Banner](assets/banner.svg)")
content = content.replace("## Curriculum Learning in AI", "## 🧠 Curriculum Learning in AI")
content = content.replace("## 1. The Macro Chronological Evolution", "## 🕒 1. The Macro Chronological Evolution")
content = content.replace("## 2. Core Operational & Scheduling Variants", "## ⚙️ 2. Core Operational & Scheduling Variants")
content = content.replace("## 3. High-Capacity Architectural", "## 🏗️ 3. High-Capacity Architectural")
content = content.replace("## 4. Production Engineering Challenges", "## 🚧 4. Production Engineering Challenges")
content = content.replace("## 5. Frontier Real-World", "## 🌍 5. Frontier Real-World")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

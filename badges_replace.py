import os
import re
import sys

action = sys.argv[1]

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

if action == "seo_badges_left":
    left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
    # Insert under heading
    content = re.sub(r"(# 🚀 Awesome-Curriculum-Learning 🚀\n\n!\[Banner\]\(assets/banner.svg\))", r"\1\n\n" + left_badges, content)
    # SEO
    content = content.replace("## 🧠 Curriculum Learning in AI", "## 🧠 Curriculum Learning in AI: The Ultimate SEO-Optimized Guide")
    
elif action == "badges_right":
    right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
    # insert next to left badges
    content = content.replace('alt="Discord" /></a>', 'alt="Discord" /></a>' + right_badge)

elif action == "star_history":
    star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Curriculum-Learning&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Curriculum-Learning&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Curriculum-Learning&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Curriculum-Learning&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
    content = content + "\n" + star_history

elif action == "fix_star_plot":
    content = content.replace("chartrepos", "chart?repos")

elif action == "fix_awesome":
    content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)


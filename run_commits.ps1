python tabularize_and_pages.py
git add .
git commit -m "tabularised the bullets"

git add pages\
git commit -m "detailed pages created"

python decorate.py
git add .
git commit -m "added emojis and banner"

python badges_replace.py seo_badges_left
git add .
git commit -m "seo optimised and badges to left added"

python badges_replace.py badges_right
git add .
git commit -m "badges to right added"

python badges_replace.py star_history
git add .
git commit -m "star history added"

python badges_replace.py fix_star_plot
git add .
git commit -m "fixed star plot"

python badges_replace.py fix_awesome
git add .
git commit -m "invalid awesome link fixed"

git push

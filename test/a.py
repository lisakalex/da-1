import requests
import time
from pathlib import Path
import shutil
from datetime import datetime
import os
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup

# fix Recommended to do
with open('./b/index.html', 'r') as f:
    soup = BeautifulSoup(f.read(), features="html.parser")

recommended = soup.findAll('ul', class_="header-menu__dropdown-children")
recommended = recommended[4]

recommended_1 = soup.findAll('ul', class_="sub-menu")
recommended_1 = recommended_1[5]

footer = soup.findAll('div', class_="header-menu__dropdown-children")
footer = footer[5]

with open('./me-index.html', 'r') as ff:
    soup1 = BeautifulSoup(ff.read(), features="html.parser")

editorsPicks = soup1.findAll('ul', class_="header-menu__dropdown-children")
editorsPicks = editorsPicks[3]

editorsPicks_1 = soup1.findAll('ul', class_="sub-menu")
editorsPicks_1 = editorsPicks_1[3]

editorsPicks_footer = soup1.findAll('div', class_="header-menu__dropdown-children")
editorsPicks_footer = editorsPicks_footer[3]

if recommended and editorsPicks:
    editorsPicks.replace_with(recommended)

if recommended_1 and editorsPicks_1:
    editorsPicks_1.replace_with(recommended_1)

if footer and editorsPicks_footer:
    editorsPicks_footer.replace_with(footer)

# links = soup1.findAll('a')
for link in soup1.findAll('a'):
    href = link.get('href')
    if href:
        if 'https://cryptonews.com' in href:
            href = href.replace('https://cryptonews.com', '')
            link['href'] = href

with open('./me-index.html', "w") as file:
    file.write(str(soup1))

huy = None

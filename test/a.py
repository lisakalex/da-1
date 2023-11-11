import requests
import time
from pathlib import Path
import shutil
from datetime import datetime
import os
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup

# def no_lazy_loading(read_file1):
with open('index.html', 'r') as file1:
    soup = BeautifulSoup(file1.read(), features="html.parser")

lazy = soup.findAll('img')
for la in lazy:
    if la.has_attr('data-src'):
        la['src'] = la['data-src']

    if la.has_attr('data-lazy-src'):
        la['src'] = la['data-lazy-src']

    # script_tags = soup.find_all('script', data-src=True)
# tag = soup.findAll('script', data-src=True)
# lazy = soup.findAll('img', data-src=True)
# if lazy['data-src'] is not None:
#     soup1.body.insert(1, se_pre_con)
#
# for dslot in soup1.findAll('div', class_='dslot'):
#     for medslot in soup.findAll('div', class_='dslot'):
#         if dslot.get('did') == medslot.get('did'):
#             dslot.replace_with(medslot)
#
# with open('./me-index.html', "w") as file:
#     file.write(str(soup1))

huy = None

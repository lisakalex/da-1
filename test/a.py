import requests
import time
from pathlib import Path
import shutil
from datetime import datetime
import os
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup


# with open('./index.htm', 'r') as file:
#     contact = file.read()
#
# with open('./index.php', "a") as file:
#     file.write(contact)

# def insert_load_tag(read_file1):
# with open('me-index.html', 'r') as file1:
with open('/var/www/da-1.com/me-index.html') as file:
    soup = BeautifulSoup(file, features='html.parser')

with open('a.html') as file:
    soup1 = BeautifulSoup(file, features='html.parser')

se_pre_con = soup.find('div', class_='se-pre-con')
soup1.body.insert(1, se_pre_con)

with open('a.html', "w") as file:
    file.write(str(soup1))

huy = None

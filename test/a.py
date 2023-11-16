import requests
import time
from pathlib import Path
import shutil
from datetime import datetime
import os
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup


def insert_in_head(read_file1):
    soup = BeautifulSoup("<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js\"></script>", features='html.parser')
    script = soup.script
    soup = BeautifulSoup("<script defer="" src=\"/assets/js/frontend.js\"></script>", features='html.parser')
    script1 = soup.script
    soup1 = BeautifulSoup(read_file1, features='html.parser')

    if soup1.head is not None:
        soup1.head.insert(1, script)
        soup1.head.insert(2, script1)

    return str(soup1)


with open('index.html') as file:
    read_file = file.read()

read_file = insert_in_head(read_file)

with open('index.html', "w") as file:
    file.write(read_file)
huy = None

import requests
import time
from pathlib import Path
import shutil
from datetime import datetime
import os
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file, features='html.parser')
    soup.find(text="cryptonews").replace_with('<data class="replace-1" value=""></data>')
    soup.find(text="Cryptonews").replace_with('<data class="replace-2" value=""></data>')
    soup.find(text="CryptoNews").replace_with('<data class="replace-3" value=""></data>')
    soup.find(text="CRYPTONEWS").replace_with('<data class="replace-4" value=""></data>')

huy = None

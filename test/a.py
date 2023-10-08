import requests
import time
from pathlib import Path
import shutil
from datetime import datetime
import os
import subprocess
from pathlib import Path

with open('./index.htm', 'r') as file:
    contact = file.read()

with open('./index.php', "a") as file:
    file.write(contact)

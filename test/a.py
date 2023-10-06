import requests
import time
from pathlib import Path
import shutil
from datetime import datetime
import os
import subprocess
from pathlib import Path


for item in os.listdir('/var/www/da-1.com/test/kak'):
    os.symlink('/var/www/da-1.com/test/kak' + item, '/var/www/da-1.com/test/kak1/' + item)

# dst = args[-1]
# for src in args[:-1]:
#     os.symlink(src, os.path.join(dst, os.path.dirname(src)))

# subprocess.call(["ln", "-s", "/var/www/da-1.com/test/kak/*", "/var/www/da-1.com/test/kak1"])

# Path('/var/www/da-1.com/test/kak1/').symlink_to('/var/www/da-1.com/test/kak/*')

# subprocess.call(["ls", "-l"])
# src = 'test/kak/*'
# dst = 'test/kak1'
# os.chdir('/var/www/da-1.com/')
# os.symlink(src, dst)

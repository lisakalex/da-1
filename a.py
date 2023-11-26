#!/home/al/.venv/bin/python3
from datetime import datetime

with open('zuy', "w") as file:
    file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '\n')

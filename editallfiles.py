#!/home/al/.venv/bin/python3
import glob2
from bs4 import BeautifulSoup
import requests
import time
import shutil
from datetime import datetime

# https://beautiful-soup-4.readthedocs.io/en/latest/

start_time = time.time()
todaytime = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
source = None

try:
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    source = requests.get('https://cryptonews.com/', headers=headers, timeout=None)

except Exception as e:
    print(e)
    pass

with open('./a/cryptonews.com/index.html', "w") as file:
    file.write(source.text)

shutil.rmtree('./b/', ignore_errors=True)
shutil.rmtree('./html', ignore_errors=True)
shutil.copytree('./a/cryptonews.com', './b/', dirs_exist_ok=True)
shutil.copytree('./replace/', './b/', dirs_exist_ok=True)

# in case these are downloaded delete them
shutil.rmtree('./b/tags/', ignore_errors=True)
shutil.rmtree('./b/events/', ignore_errors=True)
shutil.rmtree('./b/jobs/', ignore_errors=True)
shutil.rmtree('./b/price-tracker/', ignore_errors=True)
shutil.rmtree('./b/videos/', ignore_errors=True)
shutil.rmtree('./b/video_categories/', ignore_errors=True)
shutil.rmtree('./b/wp-content/', ignore_errors=True)
shutil.rmtree('./b/wp-includes/', ignore_errors=True)
shutil.rmtree('./b/wp-json/', ignore_errors=True)


def replace_header_footer(read_file1):
    with open('./replace/me-index.html', 'r') as file1:
        soup = BeautifulSoup(file1.read(), features="html.parser")

    # head = soup.find("head")
    header = soup.find("header")
    footer = soup.find("footer")

    soup1 = BeautifulSoup(read_file1, features="html.parser")

    # head1 = soup1.find("head")
    # if head1:
    #     head1.replace_with(head)

    header1 = soup1.find("header")
    if header1:
        header1.replace_with(header)

    footer1 = soup1.find("footer")
    if footer1:
        footer1.replace_with(footer)

    return str(soup1)


def insert_in_head(read_file1):
    soup = BeautifulSoup("<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js\"></script>", features='html.parser')
    script = soup.script

    soup = BeautifulSoup("<script defer src=\"/assets/js/me.js\"></script>", features='html.parser')
    script1 = soup.script

    soup = BeautifulSoup("<link href=\"/assets/css/style.css\" rel=\"stylesheet\">", features='html.parser')
    script2 = soup.link

    soup1 = BeautifulSoup(read_file1, features='html.parser')

    if soup1.head is not None:
        soup1.head.insert(100, script)
        soup1.head.insert(101, script1)
        soup1.head.insert(102, script2)

    return str(soup1)


files = ['html', 'htm']
count_replace = 1

for fl in files:
    for filepath in glob2.iglob('./b/**/*.' + fl, recursive=True):
        print(str(count_replace) + ' ' + filepath)
        with open(filepath) as file:
            read_file = file.read()

        read_file = replace_header_footer(read_file)
        read_file = insert_in_head(read_file)
        count_replace = count_replace + 1

        with open(filepath, "w") as file:
            file.write(read_file)

shutil.copytree('./b/', './html/', dirs_exist_ok=True)
shutil.copyfile('./a/cryptonews.com/index.html', './html/kak-index.html')  # used to update recommended
finish_time = time.time() - start_time
finish_time = round(finish_time / 60, 2)

print('copied ' + str(count_replace) + ' files, time taken ' + str(finish_time) + ' min')

with open('count_replace.txt', "a") as file:
    file.write(todaytime + ' files ' + str(count_replace) + ', time ' + str(finish_time) + ' min\n')

ha = None

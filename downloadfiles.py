#!/home/al/.venv/bin/python3
import glob2
from bs4 import BeautifulSoup
import requests
import time
import shutil
from datetime import datetime
from pathlib import Path

# https://beautiful-soup-4.readthedocs.io/en/latest/

with open('count_download.txt', "w") as file:
    file.write('')

source = None
start_time = time.time()
start_time1 = time.time()
count_replace = 0
try:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    source = requests.get('https://cryptonews.com/', headers=headers, timeout=None)

except Exception as e:
    print(e)
    pass

Path('./a/cryptonews.com/news/').mkdir(parents=True, exist_ok=True)

if source.status_code == 200:
    try:
        with open('./a/cryptonews.com/index.html', "w") as file:
            file.write(source.text)

    except Exception as e:
        print(e)
        pass

    count_replace = count_replace + 1

    with open('count_download.txt', "a") as file:
        file.write(str(count_replace) + ' ' + str(source.status_code) + ' ' + str(
            round(time.time() - start_time, 3)) + ' /index.html\n')
        print(str(count_replace) + ' ' + str(source.status_code) + ' ' + str(
            round(time.time() - start_time, 3)) + ' /index.html')

soup = BeautifulSoup(source.text, features="html.parser")
sub_menu = soup.findAll('ul', class_='sub-menu')

for a in sub_menu[12].findAll('a'):
    link = a.get('href')
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
        source = requests.get(link, headers=headers, timeout=None)

    except Exception as e:
        print(e)
        pass

    if source.status_code == 200:
        link = link.replace("https://cryptonews.com", "")
        with open('./a/cryptonews.com' + link, "w") as file:
            file.write(source.text)

        count_replace = count_replace + 1

        with open('count_download.txt', "a") as file:
            file.write(str(count_replace) + ' ' + str(source.status_code) + ' ' + str(
                round(time.time() - start_time, 3)) + ' ' + link + '\n')
            print(str(count_replace) + ' ' + str(source.status_code) + ' ' + str(
                round(time.time() - start_time, 3)) + ' ' + link)

shutil.copyfile('./a/cryptonews.com/index.html', './kak-index.html')  # used to update recommended
shutil.copytree('./replace/', './a/cryptonews.com/', dirs_exist_ok=True)


def download_file(f1):
    start_time = time.time()
    source = None
    global count_replace
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    try:
        source = requests.get('https://cryptonews.com' + f1, headers=headers, timeout=None)

    except Exception as e:
        print(e)
        pass
    if source.status_code == 200:
        Path('./a/cryptonews.com' + f1).mkdir(parents=True, exist_ok=True)
        with open('./a/cryptonews.com' + f1 + 'index.html', "w") as file:
            file.write(source.text)

        count_replace = count_replace + 1
        with open('count_download.txt', "a") as file:
            file.write(str(count_replace) + ' ' + str(source.status_code) + ' ' + str(
                round(time.time() - start_time, 3)) + ' ' + f1 + 'index.html\n')
            print(str(count_replace) + ' ' + str(source.status_code) + ' ' + str(
                round(time.time() - start_time, 3)) + ' ' + f1 + 'index.html')

    for i in range(2, 10):
        start_time = time.time()
        try:
            url = 'https://cryptonews.com' + f1 + 'page/' + str(i) + '/'
            source = requests.get(url, headers=headers, timeout=None)

        except Exception as e:
            print(e)
            pass
        if source.status_code == 200:
            try:
                Path('./a/cryptonews.com' + f1 + 'page/' + str(i) + '/').mkdir(parents=True, exist_ok=True)
                with open('./a/cryptonews.com' + f1 + 'page/' + str(i) + '/index.html', "w") as file:
                    file.write(source.text)

            except Exception as e:
                print(e)
                pass

            count_replace = count_replace + 1
            with open('count_download.txt', "a") as file:
                file.write(str(count_replace) + ' ' + str(source.status_code) + ' ' + str(
                    round(time.time() - start_time, 3)) + ' ' + f1 + 'page/' + str(i) + '/index.html\n')
                print(str(count_replace) + ' ' + str(source.status_code) + ' ' + str(
                    round(time.time() - start_time, 3)) + ' ' + f1 + 'page/' + str(i) + '/index.html')

        soup = BeautifulSoup(source.text, features="html.parser")
        article = soup.findAll('article')

        for a in article:
            start_time = time.time()
            article = a.find('a').get('href')

            try:
                source = requests.get(article, headers=headers, timeout=None)

            except Exception as e:
                print(e)
                pass

            article = article.replace("https://cryptonews.com", "")

            if source.status_code == 200:
                try:
                    with open('./a/cryptonews.com' + article, "w") as file:
                        file.write(source.text)

                except Exception as e:
                    print(e)
                    pass
                count_replace = count_replace + 1
                with open('count_download.txt', "a") as file:
                    file.write(str(count_replace) + ' ' + str(source.status_code) + ' ' + str(
                        round(time.time() - start_time, 3)) + ' ' + article + '\n')
                    print(str(count_replace) + ' ' + str(source.status_code) + ' ' + str(
                        round(time.time() - start_time, 3)) + ' ' + article)


file_list = ['/news/',
             '/news/altcoin-news/',
             '/news/bitcoin-news/',
             '/news/blockchain-news/',
             '/news/cryptonews-deals/',
             '/news/defi-news/',
             '/news/ethereum-news/',
             '/news/finance-news/',
             '/news/ico-news/',
             '/news/industry-talk/',
             '/news/nft-news/',
             '/news/press-releases/',
             '/news/price-predictions/',
             '/news/sponsored/',
             '/news/technology-news/',
             '/exclusives/',
             '/exclusives/features/',
             '/exclusives/opinions/',
             '/exclusives/people/']

for f in file_list:
    download_file(f)

with open('count_download.txt', "a") as count:
    count.write('time ' + str(round((time.time() - start_time1) / 60, 2)) + '\n')
    print('time ' + str(round((time.time() - start_time1) / 60, 2)) + ' min')

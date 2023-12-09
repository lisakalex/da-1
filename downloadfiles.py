#!/home/al/.venv/bin/python3
import glob2
from bs4 import BeautifulSoup
import requests
import time
import shutil
from datetime import datetime


# https://beautiful-soup-4.readthedocs.io/en/latest/

def download_file(f1):
    start_time = time.time()
    source = None
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
        source = requests.get('https://cryptonews.com' + f1, headers=headers, timeout=None)

    except Exception as e:
        print(e)
        pass

    with open('./a/cryptonews.com' + f1 + 'index.html', "w") as file:
        file.write(source.text)

    with open('count_replace.txt', "w") as file:
        file.write(f1 + ' ' + str(source.status_code) + ' ' + str(round(time.time() - start_time, 2)) + '\n')

    for i in range(2, 4):
        start_time = time.time()
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
            url = 'https://cryptonews.com' + f1 + 'page/' + str(i) + '/'
            source = requests.get(url, headers=headers, timeout=None)

        except Exception as e:
            print(e)
            pass

        try:
            with open('./a/cryptonews.com' + f1 + 'page/' + str(i) + '/index.html', "w") as file:
                file.write(source.text)

        except Exception as e:
            print(e)
            pass

        with open('count_replace.txt', "a") as file:
            file.write(f1 + 'page/' + str(i) + '/ ' + str(source.status_code) + ' ' + str(round(time.time() - start_time, 2)) + '\n')

        soup = BeautifulSoup(source.text, features="html.parser")
        article = soup.findAll('article')
        for a in article:
            start_time = time.time()
            article = a.find('a').get('href')

            try:
                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
                source = requests.get(article, headers=headers, timeout=None)

            except Exception as e:
                print(e)
                pass

            article = article.replace("https://cryptonews.com", "")

            try:
                with open('./a/cryptonews.com' + article, "w") as file:
                    file.write(source.text)

            except Exception as e:
                print(e)
                pass

            with open('count_replace.txt', "a") as file:
                file.write(f1 + ' ' + str(source.status_code) + ' ' + str(round(time.time() - start_time, 2)) + '\n')


start_time1 = time.time()

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

with open('count_replace.txt', "w") as count:
    count.write('time ' + str(round((time.time() - start_time1) / 60, 2)) + '\n')

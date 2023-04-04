import requests
from bs4 import BeautifulSoup

url = 'https://glints.com/id/lowongan-kerja'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

res = requests.get(url)
print(res.status_code)

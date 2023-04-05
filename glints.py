import os

import requests
from bs4 import BeautifulSoup

url = 'https://www.loker.id/cari-lowongan-kerja/?'
params = {
    'q': 'manager',
    'lokasi': 0,
    'category': 0,
    'pendidikan': 0
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

#res = requests.get(url, headers=headers)
#soup = BeautifulSoup(res.text, 'html.parser')


def get_total_page():
    res = requests.get(url, params=params, headers=headers)

    """
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()
    """

    #scrap
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find_all('ul', 'pagination pagination-sm')
    print(pagination)


if __name__ == '__main__':
    get_total_page()
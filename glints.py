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

res = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
try:
    os.mkdir('temp')
except FileExistsError:
    pass

with open('temp/res.html', 'w+') as outfile:
    outfile.write(res.text)
    outfile.close()


def get_total_page():
    total_page = []
    pagination = soup.find('ul', 'pagination pagination-sm')
    pages = pagination.find_all('li')
    for page in pages:
        total_page.append(page.text)

    del total_page[-1]
    del total_page[-1]

    total = int(max(total_page))
    print(total)
    return total


def get_content():
    contents = soup.find('div', 'm-b-40')
    # loker
    # perusahaan
    # pendidikan
    # lokasi
    """
    all_loker = contents.find_all('h3', 'media-heading h4')

    for i in all_loker:
        loker = i.find('a').text
        print(loker)
    """

    table = contents.find_all('table', 'table')
    for i in table:
        items = i.findAll('tr')

        perusahaan = items[0]
        perusahaan = perusahaan.findAll('td')
        perusahaan = str(perusahaan[1])
        perusahaan = perusahaan.replace('<td>','').replace('</td>','')
        print(perusahaan)

        pendidikan = items[1]
        pendidikan = pendidikan.findAll('td')
        pendidikan = str(pendidikan[1])
        pendidikan = pendidikan.replace('<td>', '').replace('</td>', '')
        print(pendidikan)

        lokasi = items[2]
        lokasi = lokasi.findAll('td')
        lokasi = str(lokasi[1])
        lokasi = lokasi.replace('<td>', '').replace('</td>', '')
        print(lokasi)

        print()
        # for i in perusahaan:
        #    print(i)


if __name__ == '__main__':
    get_content()

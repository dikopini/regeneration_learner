import requests
from bs4 import BeautifulSoup


def coba(page):
    url = (f'https://www.loker.id/cari-lowongan-kerja/page/{page}?')

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
    contents = soup.find('div', 'm-b-40')
    all_loker = contents.find_all('h3', 'media-heading h4')
    a = 0

    table = contents.find_all('table', 'table')
    job_list = []
    for i in table:
        job = all_loker[a].find('a').text
        a = a + 1

        items = i.findAll('tr')

        perusahaan = items[0]
        perusahaan = perusahaan.findAll('td')
        perusahaan = str(perusahaan[1])
        perusahaan = perusahaan.replace('<td>', '').replace('</td>', '')

        pendidikan = items[1]
        pendidikan = pendidikan.findAll('td')
        pendidikan = str(pendidikan[1])
        pendidikan = pendidikan.replace('<td>', '').replace('</td>', '')

        lokasi = items[2]
        lokasi = lokasi.findAll('td')
        lokasi = str(lokasi[1])
        lokasi = lokasi.replace('<td>', '').replace('</td>', '')

        data_dict = {
            'lowongan kerja': job,
            'perusahaan': perusahaan,
            'pendidikan': pendidikan,
            'lokasi': lokasi
        }
        job_list.append(data_dict)
    return job_list
        #print(data_dict)


def run():
    total_page = 5
    counter = 0
    final_result = []

    for i in range(total_page):
        counter +=1
        final_result += coba(counter)
        print(counter)
        print(final_result)


if __name__ == '__main__':
    run()
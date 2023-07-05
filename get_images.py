import os.path
import urllib.request

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

URL = "https://phonoteka.org/44628-krasnouhaja-cherepaha-oboi.html/"  # ссылка на сайт, откуда будут взяты изображения
FOLDER = "images"  # папка, где будут храниться изображения


def get_image(url):
    f = urllib.request.urlopen(url)
    page = f.read()
    f.close()
    soup = BeautifulSoup(page, 'lxml')
    urls = []

    for link in soup.findAll('img'):
        img_url = link.get('data-src')
        if img_url:
            urls.append(f'https://phonoteka.org{img_url}')

    return urls  # возвращаем список ссылок на изображения из сайта


def download(url, pathname):
    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    response = requests.get(url, stream=True)
    filename = os.path.join(pathname, url.split('/')[-1])  # создадим файл внутри папки, куда запишем биты изображения

    progress = tqdm(response.iter_content(1024))  # скачаем изображения в ранее созданный файл в папке
    with open(filename, "wb") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))


def main(url, pathname):
    urls = get_image(url)
    for url in urls:
        download(url, pathname)


main(URL, FOLDER)

import requests

from Multithreading_and_Multiprocessing.Module_threading.decorators import measure_time


def download_site(url, session):
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')


@measure_time
def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == '__main__':
    sites = [
                "https://www.google.com/",
                "https://www.python.org/",
            ] * 80  # 160 копій сайтів

    download_all_sites(sites)

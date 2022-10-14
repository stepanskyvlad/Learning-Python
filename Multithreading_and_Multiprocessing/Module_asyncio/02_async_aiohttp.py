import asyncio
import aiohttp

from Multithreading_and_Multiprocessing.Module_threading.decorators import async_measure_time


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.thumbnail_url = thumbnail_url
        self.url = url
        self.title = title
        self.photo_id = photo_id
        self.album_id = album_id

    # метод, який парсить шматок JSON і повертає об'єкт фотографії
    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


# допоміжний метод, який виводить титульники фотографій
def print_photo_titles(photos):
    for photo in photos:
        print(f"{photo.title}", end='\n')


# метод, який працює з HTTP асинхронно, який буде викачувати дані по деякій адресі
async def photos_by_album(task_name, album, session):
    print(f"{task_name=}")
    url = f"https://jsonplaceholder.typicode.com/photos?albumId={album}"

    response = await session.get(url)
    photos_json = await response.json()

    return [Photo.from_json(photo) for photo in photos_json]


@async_measure_time
async def main():
    # async with aiohttp.ClientSession() as session:
    #     photos = await photos_by_album('Task 1', 3, session)
    #     print_photo_titles(photos)

    # порахувати кількість фотографій в альбомах
    async with aiohttp.ClientSession() as session:
        photos_in_albums = await asyncio.gather(*(photos_by_album(f"Task {i + 1}", album, session)
                                                  for i, album in enumerate(range(2, 30))))
        photos_count = sum([len(cur) for cur in photos_in_albums])
        print(f"{photos_count=}")


if __name__ == "__main__":
    asyncio.run(main())

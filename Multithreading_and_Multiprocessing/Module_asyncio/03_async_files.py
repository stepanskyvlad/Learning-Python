import asyncio
import aiofiles


def read_large_file():
    with open('..\\data\\big_file.txt', 'r') as f:
        return f.read()


# поки йде вичитка файлу, якісь інші карутини можуть щось робити
async def async_read_large_file():
    async with aiofiles.open('..\\data\\big_file.txt', 'r') as f:
        return await f.read()


def count_words(text):
    return len(text.split(' '))


# асинхронне виконання програми
async def async_main():
    text = await async_read_large_file()
    print(count_words(text))


# послідовне виконання програми
def main():
    text = read_large_file()
    print(count_words(text))


if __name__ == "__main__":
    asyncio.run(async_main())
    main()

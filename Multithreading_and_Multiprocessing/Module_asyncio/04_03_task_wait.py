import asyncio
from asyncio import FIRST_COMPLETED
from collections import namedtuple

import aiohttp

# описує сервіс, який визначає API
Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

# список сервісів
services = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


# метод який бере JSON по URL
async def get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


# метод який витягує API із JSON
async def fetch_ip(service):
    print(f'Fetching IP from {service.name}')

    json_response = await get_json(service.url)
    ip = json_response[service.ip_attr]
    return f'{service.name} finished with result: {ip}'


async def main():
    coroutines = [fetch_ip(service) for service in services]

    # return_when=FIRST_COMPLETED - flag працює таким чином, коли закінчилися одна із задач,
    # то інші скасовуються
    done, pending = await asyncio.wait(coroutines, return_when=FIRST_COMPLETED)

    for x in done:
        print(x.result())


if __name__ == '__main__':
    asyncio.run(main())

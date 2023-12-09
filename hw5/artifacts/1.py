import aiohttp
import asyncio
import os


async def download_image(session: aiohttp.ClientSession, url: str, file_name: str) -> None:
    async with session.get(url) as response:
        if response.status == 200:
            with open(file_name, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)


async def download_images(url: str, count: int, folder: str) -> None:
    os.makedirs(folder, exist_ok=True)
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(download_image(session, url, os.path.join(folder, f'image_{i}.jpg'))) for i in
                 range(count)]
        await asyncio.gather(*tasks)


def main() -> None:
    url = 'https://thispersondoesnotexist.com/'
    count = 5
    folder = 'hw5/artifacts/images'

    asyncio.run(download_images(url, count, folder))


if __name__ == '__main__':
    main()

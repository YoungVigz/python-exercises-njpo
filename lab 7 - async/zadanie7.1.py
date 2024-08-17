import aiohttp
import asyncio
from tqdm.asyncio import tqdm_asyncio

async def fetch_photos(session, query, num_photos):
    url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": "Client-ID KLUCZ" # W miejscu KLUCZ trzeba podać API KEY z konta deweloperskiego unsplash
    }

    params = {
        "query": query,
        "per_page": num_photos
    }

    try:
        async with session.get(url, headers=headers, params=params) as response:
            response.raise_for_status()
            data = await response.json()
            return data['results']
    except aiohttp.ClientError as e:
        print(f"Nie udało się znaleźć zdjęć")
        return None

async def download_photo(session, photo):
    try:
        photo_url = photo['urls']['small']
        photo_id = photo['id']
        async with session.get(photo_url) as response:
            response.raise_for_status()
            with open(f"{photo_id}.jpg", 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
    except Exception as e:
        print(f"Nie udało się pobrać zdjęć")   

async def main():
    query = input("Podaj słowo kluczowe: ")
    num_photos = 5

    async with aiohttp.ClientSession() as session:
        photos = await fetch_photos(session, query, num_photos)
        if photos is None:
            print("Pobranie nie powowiodło się spróbuj ponownie później, lub użyj innego słowa kluczowego")
            return

        print("Szukanie zdjęć:")
        tasks = [download_photo(session, photo) for photo in photos]
        await tqdm_asyncio.gather(*tasks, desc="Pobieranie", unit="photo")

if __name__ == "__main__":
    asyncio.run(main())
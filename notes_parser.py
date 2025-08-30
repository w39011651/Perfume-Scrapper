from bs4 import BeautifulSoup
import perfume_parser
import asyncio, aiohttp
from save_csv import save_to_csv
from utils import log

async def fetch_url(session:aiohttp.ClientSession, url:str, semaphore, delay_after_request = 0.5):
    async with semaphore:
        log(f"開始請求{url}")
        async with session.get(url) as response:
            log(f"Status (aiohttp): {response.status}")
            if delay_after_request > 0:
                await asyncio.sleep(delay_after_request)

            return await response.text()

async def main_aiohttp(data:dict):

    CONCURRENCY_LIMIT = 3
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    # 設定每個請求完成後的延遲（秒）
    DELAY_PER_REQUEST = 0.5 # 例如1秒
    tasks = []
    # 設定請求頭，模擬瀏覽器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        urls = []
        notes_data = {}
        for v in data.values():
            urls.append(v['url'])

        tasks = [fetch_url(session, url, semaphore, DELAY_PER_REQUEST) for url in urls]
        results = await asyncio.gather(*tasks)
        
        for result in results:
            soup = BeautifulSoup(result, 'lxml')
            #先將<br/>換成'\n'
            for br in soup.find_all("br"):
                br.replace_with(' ')

            product_name = soup.find('h1', class_='Product-title')
            notes = soup.find('p', class_='Product-summary Product-summary-block')
            
            notes_data[product_name.text] = notes.text.split(' ')[::2]
        
        return notes_data

        


if __name__ == '__main__':
    data = perfume_parser.get_perfumes_url()

    # Construct dictionary: {"Perfume name":{"Front notes":["A", "B", "C"], "Middle notes":["D", "E", "F"], "Base notes":["G", "H", "I"]}}

    notes_data = asyncio.run(main_aiohttp(data))

    save_to_csv(notes_data)


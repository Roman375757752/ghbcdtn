import aiohttp
import asyncio
import sys

sys.stdout.reconfigure(encoding='utf-8')

def load_proxies_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

async def fetch_with_proxy_auth(url, proxy_url, session):
    try:
        async with session.get(url, proxy=proxy_url, timeout=10) as response:
            if response.status == 200:
                print(f"Подключение через прокси успешно: {proxy_url}")
                return f"Подключение через прокси успешно: {proxy_url}"
            else:
                print(f"Не удалось подключиться через прокси: {proxy_url}")
    except Exception as e:
        print(f"Ошибка подключения через прокси: {proxy_url} — {e}")
    return None


async def main(url):
    # Загрузка прокси из файлов
    proxy_files = {
        'socks5': 'socks5.txt',
        'socks4': 'socks4.txt',
        'http': 'http.txt'
    }
    
    results = []

    for proxy_type, filename in proxy_files.items():
        proxies = load_proxies_from_file(filename)
        print(f"Загружено {len(proxies)} прокси из файла {filename}")
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            for proxy in proxies:
                proxy_url = f"{proxy_type}://{proxy}"
                tasks.append(fetch_with_proxy_auth(url, proxy_url, session))
            
            results += [result for result in await asyncio.gather(*tasks) if result]

    with open('results.txt', 'w', encoding='utf-8') as result_file:
        for line in results:
            result_file.write(line + '\n')
    print("Результаты записаны в файл results.txt")

# URL для тестирования
url = "https://slay-award.ru"  

asyncio.run(main(url))

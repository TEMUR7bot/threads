import requests
import json
from concurrent.futures import ThreadPoolExecutor


urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
    "https://jsonplaceholder.typicode.com/posts/6",
    "https://jsonplaceholder.typicode.com/posts/7",
    "https://jsonplaceholder.typicode.com/posts/8",
    "https://jsonplaceholder.typicode.com/posts/9",
    "https://jsonplaceholder.typicode.com/posts/10"
]

def fetch_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    except Exception as e:
        return {"error": str(e), "url": url}

def fetch_all_and_save(url_list, output_file="results.json"):
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_url, url_list))

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"Natijalar '{output_file}' fayliga saqlandi.")

fetch_all_and_save(urls)

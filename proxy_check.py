import threading
import queue
import requests
import csv

BASE_URL = "https://books.toscrape.com/"
valid_proxy = []
q = queue.Queue()

LIMIT = 20

with open('proxy.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    row_count = 0

    for row in reader:
        if row_count >= LIMIT:
            break

        proxy = row[0].strip('[]')
        print(proxy)
        q.put(proxy)
        row_count += 1


def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get(f'{BASE_URL}',
                               proxies={'http': proxy,
                                        'https': proxy},
                               timeout=5)
        except:
            continue
        if res.status_code == 200:
            print(proxy)


num_threads = 10

threads = [threading.Thread(target=check_proxies) for _ in range(num_threads)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

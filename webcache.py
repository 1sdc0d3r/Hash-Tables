import urllib.request
import time


class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = time.time()


cache = {}
CACHE_TIMEOUT_SECONDS = 10


def get_data(url):
    curtime = time.time()
    print({curtime})
    if (url not in cache) or (curtime - cache[url].timestamp > CACHE_TIMEOUT_SECONDS):
        print("FETCHING FROM SERVER")
        with urllib.request.urlopen(url) as f:
            data = f.read().decode('utf-8', "ignore")
            cache[url] = CacheEntry(url, data)

    else:
        print("FETCHING FROM CACHE")
        age = time.time() - cache[url].timestamp
        print(f"Age: {age}")

    return cache[url]


def main():
    while True:
        url = input("Enter URL: ")
        entry = get_data(url)
        print(entry.data[:50])


if __name__ == "__main__":
    main()

# https://example.com

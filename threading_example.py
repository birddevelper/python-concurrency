import threading
import time

def download_page(url):
    print(f"Downloading {url} ...")
    time.sleep(2)
    print(f"Finished {url}")

urls = ["http://example.com/page1", "http://example.com/page2", "http://example.com/page3"]


threads = [threading.Thread(target=download_page, args=(url,)) for url in urls]

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All downloads complete!")

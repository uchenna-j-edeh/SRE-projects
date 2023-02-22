import requests

urls = ["http://example.com", "http://example.com/page1", "http://example.com/page2", "http://example.com/page3"]

for url in urls:
    response = requests.get(url)
    if response.status_code == 404:
        print(url, "returned a 404 error.")


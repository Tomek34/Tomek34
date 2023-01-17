import requests

url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html"

response = requests.get(url)

print(f"Status kod: {response.status_code}")

print(response.text)
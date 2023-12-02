from bs4 import BeautifulSoup
import requests
links = []
value = []
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

proxies = {
    'https': 'http://185.191.236.162:3128'
}

url = 'https://www.cian.ru/kupit-kvartiru/'
request = requests.get(url)
bs = BeautifulSoup(request.text, 'html.parser')
all_links = bs.find_all('a', class_='_93444fe79c--link--VtWj6')
for links in all_links:
    links.append(links['href'])
print(links)

for link in links:
    value.append(requests.get(link))

pbs = BeautifulSoup(value.text, 'html.parser')
all_prices = pbs.find_all('span', class_='a10a3f92e9--lineHeight_9u--limEs')
for price in all_prices:
    print(price.text)
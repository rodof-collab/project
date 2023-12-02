from bs4 import BeautifulSoup
import requests


def main():
    url = 'https://www.cian.ru/kupit-kvartiru/'

    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    links = [item['href'] for item in soup.find_all('a', class_='_93444fe79c--link--VtWj6')]
    with open('links.txt', 'w') as file:
        for link in links:
            file.write(link+'\n')

    prices = [item.text.replace(' ', '_')[:-2] for item in soup.find_all('span', {'data-mark':'MainPrice'})]
    with open('prices.txt', 'w') as file:
        for price in prices:
            file.write(price+'\n')


if __name__ == '__main__':
    main()

from bs4 import BeautifulSoup
import requests


def main():
    url = 'https://www.cian.ru/kupit-kvartiru/'

    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    links = [item['href'] for item in soup.find_all('a', class_='_93444fe79c--link--VtWj6')]
    with open('sub\\links.txt', 'w') as file:
        for link in links:
            file.write(link+'\n')

    prices = [item.text.replace(' ', '_')[:-2] for item in soup.find_all('span', {'data-mark':'MainPrice'})]
    with open('sub\\prices.txt', 'w') as file:
        for price in prices:
            file.write(price+'\n')
    sqprices = [item.text.replace(' ', '_')[:-4] for item in soup.find_all('p', {'data-mark':'PriceInfo'})]
    with open('sub\\sqprices.txt', 'w', encoding='utf-8') as file:
        for sqprice in sqprices:
            file.write(sqprice+'\n')
    districts = [item.text for item in soup.find_all('div', {'class':'_93444fe79c--labels--L8WyJ'})]
    with open ('sub\\districts.txt', 'w', encoding='utf-8') as file:
        for district in districts:
            file.write(district+'\n',)


if __name__ == '__main__':
    main()
    
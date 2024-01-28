import requests
from bs4 import BeautifulSoup
import json


def get_data(number_of_pages: int = 1) -> None:
    links = []
    prices = []
    districts = []
    for page in range(1, number_of_pages + 1):
        request = requests.get(
            f'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p={page}&region=1')
        soup = BeautifulSoup(request.text, 'html.parser')

        for item in soup.find_all('a', {'class': '_93444fe79c--link--VtWj6'}):
            links.append(item['href'])

        for item in soup.find_all('span', {'data-mark': 'MainPrice'}):
            prices.append(item.text.replace(' ', '_')[:-2])

        for item in soup.find_all('div', {'class': '_93444fe79c--labels--L8WyJ'}):
            districts.append(item.text)

    data = [
        {"Price": price, "District": district, "Link": link} for price, district, link in zip(prices, districts, links)
    ]

    with open('out\\flats.json', 'w', encoding='Utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    while True:
        try:
            pages = int(input("Pages: "))
            break
        except ValueError:
            print("Error! Invalid number of pages. Try again.")

    get_data(pages)

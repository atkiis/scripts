import requests
from bs4 import BeautifulSoup

def get_lunch_lists():
    url = 'https://www.lounaat.info/lounas/moro-sky-bar/tampere'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    menu_container = soup.find('div', id='menu')
    items = menu_container.find_all('div', class_='item') if menu_container else []

    for item in items:
        item_header = item.find('div', class_='item-header')
        if item_header:
            date = item_header.text.strip()
            print(f'{date}')
        else:
            print(' ')
        
        menu_items = item.find_all('li', class_='menu-item')
        for menu_item in menu_items:
            price = menu_item.find('p', class_='price').text.strip() if menu_item.find('p', class_='price') else 'N/A'
            dish = menu_item.find('p', class_='dish').text.strip() if menu_item.find('p', class_='dish') else 'N/A'
            info = menu_item.find('p', class_='info').text.strip() if menu_item.find('p', class_='info') else 'N/A'
            print(f'Päivän menu: {dish} ({price}) - {info}')
        
        print('-' * 40)

if __name__ == '__main__':
    get_lunch_lists()


import requests
from bs4 import BeautifulSoup
import sys


link = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
soup = BeautifulSoup(link, 'lxml')
date = str(soup.find(id='')).split('"')
usd = str(soup.find(id='R01235')).split('>')
eur = str(soup.find(id='R01239')).split('>')


def currency_rates(code):
    if code.lower() == 'date':
        print(f'\nДата {date[1]}\n')
    elif code.lower() == 'usd':
        print(f'Доллар США = {usd[10][:5]} руб., {date[1]}')
    elif code.lower() == 'eur':
        print(f'Евро       = {eur[10][:5]} руб., {date[1]}')
    else:
        print('None')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)
    currency_rates(sys.argv[1])

import requests
from bs4 import BeautifulSoup
import sys


link = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
soup = BeautifulSoup(link, 'lxml')

usd = str(soup.find(id='R01235')).split('>')
eur = str(soup.find(id='R01239')).split('>')


def currency_rates(code):
    if code.lower() == 'usd':
        print(f'Доллар США = {usd[10][:5]} руб.')
    elif code.lower() == 'eur':
        print(f'Евро       = {eur[10][:5]} руб.')
    else:
        print('None')


if __name__ == '__main__':
    currency_rates(sys.argv[1])

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style


link = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
soup = BeautifulSoup(link, 'lxml')

usd = str(soup.find(id='R01235')).split('>')
eur = str(soup.find(id='R01239')).split('>')


def currency_rates(code):
    if code.lower() == 'usd':
        print(f'Доллар США = {Fore.BLUE}{usd[10][:5]}{Style.RESET_ALL} руб.')
    elif code.lower() == 'eur':
        print(f'Евро       = {Fore.BLUE}{eur[10][:5]}{Style.RESET_ALL} руб.')
    else:
        print('None')


currency_rates('Usd')
currency_rates('EUR')
currency_rates('rub')

import requests
from bs4 import BeautifulSoup


url = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
soup = BeautifulSoup(url.text, 'lxml')
v = soup.find_all('value')
date = soup.find_all('valcurs')
date = str(date[0])
date = f'\nДата {date[14:26]}\n'


def currency_rates(code):
    if code.lower() == 'date':
        print(date)
    elif code.lower() == 'usd':
        usd = str(v[10:11])
        usd = usd[8:13]
        print(f'Доллар США = {usd} руб.')
    elif code.lower() == 'eur':
        eur = str(v[11:12])
        eur = eur[8:13]
        print(f'Евро       = {eur} руб.')
    else:
        print('None')


currency_rates('Date')
currency_rates('usd')
currency_rates('EUR')
currency_rates('rub')

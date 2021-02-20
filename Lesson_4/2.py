import requests
from bs4 import BeautifulSoup


url = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
soup = BeautifulSoup(url.text, 'lxml')
v = soup.find_all('value')


def currency_rates(code):
    if code == 'usd':
        usd = str(v[10:11])
        usd = usd[8:13]
        print(f'Доллар США = {usd} руб.')
    elif code == 'eur':
        eur = str(v[11:12])
        eur = eur[8:13]
        print(f'Евро = {eur} руб.')
    else:
        print('None')


currency_rates('usd')
currency_rates('eur')
currency_rates('rub')

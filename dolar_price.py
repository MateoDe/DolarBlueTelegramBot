import requests
import lxml.html as html
import os
import datetime

DOLAR_BLUE_URL = 'https://www.dolarhoy.com/cotizaciondolarblue'
COMPRA_XPATH = '/html/body/div/div/div/div[1]/div[1]/div[1]/h4/span/text()'
VENTA_XPATH = '/html/body/div/div/div/div[1]/div[1]/div[2]/h4/span/text()'

def get_price(link, compra, venta):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            page = response.content.decode('utf-8')
            parsed = html.fromstring(page)
            try:
                buy_price = parsed.xpath(compra)
                sell_price = parsed.xpath(venta)
                compra_venta = []
                compra_venta.append(buy_price[0])
                compra_venta.append(sell_price[0])
                return compra_venta    
            except IndexError as ve:
                print(f'Error {ve}')
                
        else:
            return ['NO DISPONIBLE', 'NO DISPONIBLE'] 
    except ValueError as ve:
        print(f'Error {ve}')

if __name__ == '__main__':
    get_price(DOLAR_BLUE_URL, COMPRA_XPATH, VENTA_XPATH)
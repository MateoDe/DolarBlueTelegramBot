import requests
import lxml.html as html
import os
import datetime
from time import sleep

def get_price(link, compra, venta):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            page = response.content.decode('utf-8')
            parsed = html.fromstring(page)
            sleep(1)
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


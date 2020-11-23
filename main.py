from dolar_price import get_price
import telebot
from time import sleep

DOLAR_BLUE_URL = 'https://dolarhoy.com/'
COMPRA_XPATH = '/html/body/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/span/text()'
VENTA_XPATH = '/html/body/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/span/text()'
TOKEN = input('Token de telegram: ')


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['precio'])
def price_message(message):	
	price = get_price(DOLAR_BLUE_URL, COMPRA_XPATH, VENTA_XPATH)
	try:
		bot.reply_to(message, f'Precio de COMPRA: {price[0]} \nPrecio de VENTA: {price[1]} \nFUENTE: DolarHoy.com')
	except:
		try:
			sleep(1)
			bot.reply_to(message, f'Precio de COMPRA: {price[0]} \nPrecio de VENTA: {price[1]} \nFUENTE: DolarHoy.com')
		except:
			sleep(5)

bot.polling()
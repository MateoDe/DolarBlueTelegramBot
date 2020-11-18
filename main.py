from dolar_price import get_price
import telebot
from time import sleep

DOLAR_BLUE_URL = 'https://www.cronista.com/MercadosOnline/dolar.html'
COMPRA_XPATH = '//*[@id="dcompra1"]/div[1]/text()'
VENTA_XPATH = '//*[@id="dventa1"]/div[1]/text()'
TOKEN = input('Token de telegram: ')


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['precio'])
def price_message(message):	
	price = get_price(DOLAR_BLUE_URL, COMPRA_XPATH, VENTA_XPATH)
	try:
		bot.reply_to(message, f'Precio de COMPRA: {price[0]} \nPrecio de VENTA: {price[1]} \nFUENTE: El Cronista \n \nAceptamos donaciones para mantener el bot en linea:\nBTC: 17oyXUTzgcznNjgw3eN72vsHHFTptKFQx1 \nETH: 0xd0e693bb20a99950777e6cf6883574e6c35c1709 \nGitHub: MateoDe')
	except:
		try:
			sleep(1)
			bot.reply_to(message, f'Precio de COMPRA: {price[0]} \nPrecio de VENTA: {price[1]} \nFUENTE: El Cronista')
		except:
			sleep(5)

bot.polling()
from dolar_price import get_price
import telebot

DOLAR_BLUE_URL = 'https://www.cronista.com/MercadosOnline/dolar.html'
COMPRA_XPATH = '//*[@id="dcompra1"]/div[1]/text()'
VENTA_XPATH = '//*[@id="dventa1"]/div[1]/text()'
TOKEN = input('Token de telegram: ')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['precio'])
def price_message(message):
	bot.reply_to(message, f'Precio de COMPRA: {get_price(DOLAR_BLUE_URL, COMPRA_XPATH, VENTA_XPATH)[0]} Precio de VENTA: {get_price(DOLAR_BLUE_URL, COMPRA_XPATH, VENTA_XPATH)[1]} FUENTE: El Cronista')

bot.polling()
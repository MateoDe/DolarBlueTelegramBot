from dolar_price import get_price
import telebot

DOLAR_BLUE_URL = 'https://www.dolarhoy.com/cotizaciondolarblue'
COMPRA_XPATH = '/html/body/div/div/div/div[1]/div[1]/div[1]/h4/span/text()'
VENTA_XPATH = '/html/body/div/div/div/div[1]/div[1]/div[2]/h4/span/text()'
TOKEN = 'YOUR TOKEN'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['precio'])
def price_message(message):
	bot.reply_to(message, f'Precio de COMPRA: {get_price(DOLAR_BLUE_URL, COMPRA_XPATH, VENTA_XPATH)[0]} Precio de VENTA: {get_price(DOLAR_BLUE_URL, COMPRA_XPATH, VENTA_XPATH)[1]}')

bot.polling()

import telebot

TOKEN = "8002268236:AAFDlQpt_GS85hyOG9B_5_67tnGYEMLZF80"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! PIXEL CS2 MARKET botiga xush kelibsiz!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Siz yozdingiz: " + message.text)

bot.infinity_polling()

import telebot

TOKEN = "8002268236:AAFDlQpt_GS85hyOG9B_5_67tnGYEMLZF80"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Bu PIXEL CS2 MARKET boti!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Siz yozdingiz: {message.text}")

bot.infinity_polling()

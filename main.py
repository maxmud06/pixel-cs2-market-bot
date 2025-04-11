import telebot

# Telegram bot token
TOKEN = "8002268236:AAFDlQpt_GS85hyOG9B_5_67tnGYEMLZF80"
bot = telebot.TeleBot(TOKEN)

# Start komandasi
@bot.message_handler(commands=['start'])
def start_handler(message):
    text = "Assalomu alaykum, bu PIXEL CS2 Market bot!\nSizga qanday yordam bera olaman?"
    bot.send_message(message.chat.id, text)

# Har qanday matnga javob
@bot.message_handler(func=lambda m: True)
def echo_handler(message):
    bot.send_message(message.chat.id, "Siz yozdingiz: " + message.text)

# Botni ishga tushirish
bot.infinity_polling()

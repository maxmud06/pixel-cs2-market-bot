
import telebot

# Yangi bot tokeni
BOT_TOKEN = "7105228469:AAE-1qt1k8fyRG7_d6cmvtd4XtFqZ2fYMKE"
bot = telebot.TeleBot(BOT_TOKEN)

# Start komandasi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Bu PIXEL CS2 Market botiga xush kelibsiz!")

# Oddiy matnlarga javob
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Siz yubordingiz: {message.text}")

# Botni boshlash
bot.infinity_polling()

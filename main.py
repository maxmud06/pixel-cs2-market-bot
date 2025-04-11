import telebot
import os

8002268236:AAFDlQpt_GS85hyOG9B_5_67tnGYEMLZF80 = os.getenv("8002268236:AAFDlQpt_GS85hyOG9B_5_67tnGYEMLZF80")
bot = telebot.TeleBot(8002268236:AAFDlQpt_GS85hyOG9B_5_67tnGYEMLZF80)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать в PIXEL CS2 MARKET!")

bot.infinity_polling()

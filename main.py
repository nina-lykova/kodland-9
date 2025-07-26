import telebot

from config import token

bot = telebot.TeleBot(token)



bot.infinity_polling()
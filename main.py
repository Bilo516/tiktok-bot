import telebot
import requests

TOKEN = "9018392241:AAH6V12qi_OS7QXW3Q2gLLBC3bGy1XncYG0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Bot is online 24/7.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

bot.infinity_polling()

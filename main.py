import telebot
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

# from config read TOKEN
TOKEN = config["telegram"]["TOKEN"]


bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


bot.infinity_polling()
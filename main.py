import requests
from config import YOURBOTTOKEN
import telebot

bot = telebot.TeleBot(YOURBOTTOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, text = 'Hello user! I am the most common Telegram bot that can send cats for all occasions! In order to get your cat, just write to the chat with the bot "Send a cat", "Cat".')

@bot.message_handler(content_types = ['text'] )
def ping(message):
    if 'Send a cat' in message.text or 'send a cat' in message.text or 'Cat' in message.text or 'cat' in message.text:
         response = requests.get('https://api.thecatapi.com/v1/images/search')
         cat_url = response.json()[0]['url']
         bot.send_photo(message.chat.id, photo=cat_url)
bot.polling(none_stop=True, interval=0)

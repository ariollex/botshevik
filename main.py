from dotenv import load_dotenv
from telebot import types
import telebot
import os

# Fetching telegram bot token
load_dotenv()
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))


@bot.message_handler(commands=['start'])
def start_message(message):
    text_first = '''Привет! Я чат бот "Найти борщевик!☝️"
Ты хочешь больше узнать о бощевике 
или сообщить о собственной находке?'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_know = types.KeyboardButton("Узнать")
    button_tell = types.KeyboardButton("Сообщить")
    markup.add(button_know, button_tell)
    bot.send_message(message.chat.id, text_first, reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Узнать":
        text_know = 'Борщевик Сосновского'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_dangerous = types.KeyboardButton("Опасность")
        button_history = types.KeyboardButton("История")
        button_return = types.KeyboardButton('Главное меню')
        markup.row(button_dangerous, button_history)
        markup.add(button_return)
        bot.send_photo(message.chat.id, open('photo.jpg', 'rb'), text_know, reply_markup=markup)

    elif message.text == 'Главное меню':
        text_meny = '''Ты хочешь больше узнать о бощевике 
или сообщить о собственной находке?'''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_find = types.KeyboardButton("Узнать")
        button_know = types.KeyboardButton("Сообщить")
        markup.add(button_know, button_find)
        bot.send_message(message.chat.id, text_meny, reply_markup=markup)

    elif message.text == 'Опасность':
        text_dangerous = 'Опасность борщевика в его агресивности...'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_history = types.KeyboardButton("История")
        button_return = types.KeyboardButton('Главное меню')
        markup.add(button_history, button_return)
        bot.send_message(message.chat.id, text_dangerous, reply_markup=markup)

    elif message.text == 'История':
        text_dangerous = 'Борщевик Сосновского был разработан в СССР для кормления козлов...'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_dangerous = types.KeyboardButton("Опасность")
        button_return = types.KeyboardButton('Главное меню')
        markup.add(button_dangerous, button_return)
        bot.send_message(message.chat.id, text_dangerous, reply_markup=markup)

    elif message.text == 'Сообщить':
        text_tell = 'Эта функция пока неактивна.'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_return = types.KeyboardButton('Главное меню')
        markup.add(button_return)
        bot.send_message(message.chat.id, text_tell, reply_markup=markup)


bot.infinity_polling()
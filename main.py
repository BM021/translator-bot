import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from googletrans import Translator

import database


bot = telebot.TeleBot('6389000704:AAFJlQpyT5GGSvpvCsnBw9iLq959mCObYh4')


def language_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = KeyboardButton('EN')
    button2 = KeyboardButton('RU')
    button3 = KeyboardButton('UZ')
    button4 = KeyboardButton('ES')

    kb.add(button1, button2, button3, button4)

    return kb


def translator_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = KeyboardButton('ПЕРЕВОДЧИК')
    kb.add(button1)

    return kb


def phone_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('ОТПРАВИТЬ КОНТАКТ', request_contact=True)
    kb.add(button)

    return kb


@bot.message_handler(commands=['start'])
def start_message(message):
    user = database.check_user(message.from_user.id)

    if user:
        bot.send_message(message.from_user.id, 'Чтобы начать переводить, нажмите кнопку "ПЕРЕВОДЧИК"', reply_markup=translator_button())

    else:
        text = f'Привет {message.from_user.first_name}, я бот переводчик!\nЧтобы начать отправь свой контакт используя кнопку ниже!'

        bot.send_message(message.from_user.id, text, reply_markup=phone_button())
        bot.register_next_step_handler(message, get_contact)


def get_contact(message):
    if message.contact:
        user_phone = message.contact.phone_number
        telegram_id = message.from_user.id
        username = message.from_user.username

        database.add_user(telegram_id, user_phone, username) # добавляем юзера в базу данных

        bot.send_message(message.from_user.id, 'Вы успешно прошли регистрацию, чтобы начать использовать бот нажмите "ПЕРЕВОДЧИК"', reply_markup=translator_button())

    else:
        bot.send_message(message.from_user.id, 'Отправьте контакт использую кнопку', reply_markup=phone_button())
        bot.register_next_step_handler(message, get_contact)





@bot.message_handler(content_types=['text'])
def messages(message):
    if message.text == 'переводчик':
        bot.send_message(message.from_user.id, 'Выберите на какой язык хотите перевести', reply_markup=language_buttons())
        bot.register_next_step_handler(message, get_to_ln)


def get_to_ln(message):
    to_ln = message.text

    bot.send_message(message.from_user.id, 'Введите текст который хотите перевести')
    bot.register_next_step_handler(message, get_result, to_ln)


def get_result(message, to_ln):
    pass



bot.polling()

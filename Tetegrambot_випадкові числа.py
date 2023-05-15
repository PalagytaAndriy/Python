
import requests
import telebot

TOKEN_TELEGRAM_BOT = '6040088286:AAGSR-tD1fn1xUE03c0xmzhutipK0G6rJC0'

bot = telebot.TeleBot(TOKEN_TELEGRAM_BOT)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Випадкові числа')
    bot.send_message(message.chat.id, 'Введіть три числа через кому:\n'
                                      'Мінімальне , максимальне і кількість рандомних чисел')


@bot.message_handler(content_types=['text'])
def answer_user(message):
    answ_us = message.text.replace(' ', '').split(',')
    if len(answ_us) == 3:
        incorrect_format = [i for i in answ_us if not i.isdigit()]
        if len(incorrect_format) > 0:
            bot.send_message(message.chat.id, 'Потрідно вводити лише цифри')
        else:

            start_range, end_range, numb = answ_us
            url = f'https://www.random.org/integers/?num={numb}&min={start_range}&max={end_range}&col=1&base=10&format=plain&rnd=new'
            x = requests.get(url)
            bot.send_message(message.chat.id, x.text)


    else:
        bot.send_message(message.chat.id, 'Невірний ввід')


bot.polling()

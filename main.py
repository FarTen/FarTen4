import random
rules = [import telebot
import random

bot = telebot.TeleBot('1473476701:AAGOAdbF0lbpDiMOw1_PsMn0Q780OJA3xqI')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message)
    ist = message.json["text"].split()
    for a in ist:
        bot.send_message(message.from_user.id, a)



cplayer1_input = input

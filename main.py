import telebot

bot = telebot.TeleBot('1473476701:AAGOAdbF0lbpDiMOw1_PsMn0Q780OJA3xqI')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message)
    bot.send_message(message.from_user.id, message.json["text"])


bot.polling(none_stop=True, interval=0)

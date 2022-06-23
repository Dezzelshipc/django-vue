import telebot

bot = telebot.TeleBot('5419906532:AAECPs9lomGyVosF4ffjzTQVH88XEjGW5X0')

@bot.message_handler(content_types=['text'])
def get_user_id(message):
    print(message)
    if message.from_user.is_bot == True and message.from_user.id == 850434834:
        print(message)
    # bot.send_message()

@bot.message_handler(commands=['send'])
def send_welcome(message):
	bot.send_message(message.from_user.id, message)

print("TelegramBot attached")

bot.infinity_polling()
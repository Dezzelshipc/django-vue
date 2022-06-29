import telebot
import json
from api.models import User
from api.serializers import UserTelegramSerializer

# https://t.me/DjangoVueProjBot
bot = telebot.TeleBot('5419906532:AAECPs9lomGyVosF4ffjzTQVH88XEjGW5X0')

@bot.message_handler(commands=['start', 'help'])
def help_message(message):
    bot.send_message(message.from_user.id, '''\
"Асинхронный воркер" для django-vue проекта по вебу.
После добавления вам будет приходить сообщения о новом рекорде!
/add для добавления этого чата в оповещения о пользователях.
/delete для удаления какого-то оповещения 
/clear для отчищеия списка уведомлений
''')


@bot.message_handler(commands=['add'])
def register(message):
    bot_l = telebot.types.InlineKeyboardMarkup()
    # bot_l.add(telebot.types.InlineKeyboardButton(text="Сайт", url="https://youtube.com"))
    bot.send_message(message.from_user.id, "Имя пользователя, который зарегестрирован на сайте", reply_markup=bot_l)
    bot.register_next_step_handler(message, get_register)

def get_register(message):
    try:
        user = User.objects.get(username=message.text)
    except Exception as error:
        bot.send_message(message.from_user.id, "Пользователя не существует")
        print(error)
        return

    if message.from_user.id in user.__dict__['telegram']:
        bot.send_message(message.from_user.id, "Вы уже получаете сообщения от этого пользователя")
        return
    
    data = { 'telegram': user.__dict__['telegram'] }
    data['telegram'].append(message.from_user.id)

    serializer = UserTelegramSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        bot.send_message(message.from_user.id, f"Теперь вы будете получать сообщения об успехах пользователя {message.text}.")
    else:
        bot.send_message(message.from_user.id, serializer.errors['username'])
        
@bot.message_handler(commands=['delete'])
def delete(message):
    bot_l = telebot.types.InlineKeyboardMarkup()
    # bot_l.add(telebot.types.InlineKeyboardButton(text="Сайт", url="https://youtube.com"))
    bot.send_message(message.from_user.id, "Имя пользователя, который зарегестрирован на сайте", reply_markup=bot_l)
    bot.register_next_step_handler(message, get_delete)

def get_delete(message):
    try:
        user = User.objects.get(username=message.text)
    except Exception as error:
        bot.send_message(message.from_user.id, "Пользователя не существует")
        print(error)
        return
    
    if not message.from_user.id in user.__dict__['telegram']:
        bot.send_message(message.from_user.id, "Вы не получали сообщения от этого пользователя")
        return
    
    data = { 'telegram': user.__dict__['telegram'] }
    data['telegram'].remove(message.from_user.id)

    serializer = UserTelegramSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        bot.send_message(message.from_user.id, f"Теперь вы не будете получать сообщения о {message.text}.")
    else:
        bot.send_message(message.from_user.id, serializer.errors['username'])

@bot.message_handler(commands=['clear'])
def clear(message):
    try:
        users = User.objects.filter(telegram__contains=message.from_user.id)
    except Exception as error:
        bot.send_message(message.from_user.id, "Ошибка")
        print(error)
        return

    for i in users:
        data = { 'telegram': i.__dict__['telegram'] }
        data['telegram'].remove(message.from_user.id)

        serializer = UserTelegramSerializer(i, data=data)
        if serializer.is_valid():
            serializer.save()
    
    bot.send_message(message.from_user.id, f"Теперь вы не будете получать сообщения.")


def run_bot():
    try:
        print("TelegramBot is ready")
        bot.infinity_polling()
    except Exception as error:
        print(error)

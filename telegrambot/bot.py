import telebot
from api.models import User
from api.serializers import UserTelegramSerializer

# https://t.me/DjangoVueProjBot
bot = telebot.TeleBot('5419906532:AAECPs9lomGyVosF4ffjzTQVH88XEjGW5X0')

@bot.message_handler(commands=['start', 'help'])
def help_message(message):
    bot.send_message(message.from_user.id, '''\
"Асинхронный воркер" для django-vue проекта по вебу.
После регистрации в боте вам будет приходить сообщения о новом рекорде!
/register для регистрации.
/change для изменения.
''')


@bot.message_handler(commands=['register', 'change'])
def register(message):
    bot_l = telebot.types.InlineKeyboardMarkup()
    # bot_l.add(telebot.types.InlineKeyboardButton(text="Сайт", url="https://youtube.com"))
    bot.send_message(message.from_user.id, "Введите ваш логин пользователя, который зарегестрирован на сайте", reply_markup=bot_l)
    bot.register_next_step_handler(message, get_username)

def get_username(message):
    try:
        user = User.objects.get(username=message.text)
    except Exception as error:
        bot.send_message(message.from_user.id, "Пользователя не существует")
        print(error)
        return
    data = { 'telegram': message.from_user.id }
    serializer = UserTelegramSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        bot.send_message(message.from_user.id, f"Теперь вы будете получать сообщения об успехах пользователя {message.text}.\nЕсли хотитие поменять, введите /change")
    else:
        bot.send_message(message.from_user.id, serializer.errors['username'])
        


def run_bot():
    try:
        print("TelegramBot is ready")
        bot.infinity_polling()
    except Exception as error:
        print(error)

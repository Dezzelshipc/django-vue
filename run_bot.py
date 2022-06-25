import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from telegrambot.bot import run_bot

if __name__ == "__main__":
    run_bot()
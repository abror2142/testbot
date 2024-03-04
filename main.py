from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('6933504152:AAGn8OQdYRUZzkp6zVi_ZWHLe0TgBFMHx0I')


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f"Assalomu Alaykum {full_name}")


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f"Assalomu Alaykum {full_name}")
bot.polling()

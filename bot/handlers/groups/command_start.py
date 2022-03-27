from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['start'])
async def command_start(message: Message):
    await bot.send_message(message.chat.id, f"Salom {message.from_user.full_name} siz guruhdasiz!\n")

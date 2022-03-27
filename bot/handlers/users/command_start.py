from loader import bot
from telebot.types import Message
from keyboards.inline.privateStartButtons import markupStart


@bot.message_handler(commands=['start'], chat_types=['private'])
async def command_start(message: Message):
    matn = f"<b>Assalom alaykum <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>!</b>\n"
    matn += "Senior dasturchi <a href='https://t.me/saidbekarislonov'>Saidbek Arislonov</a> o'z video darslarini YouTube sahifasiga joylagan.\n"
    await bot.send_message(chat_id=message.chat.id, text=matn, reply_markup=markupStart)

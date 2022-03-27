from loader import bot
from telebot.types import Message
from keyboards.inline.new_chat_member_keyboards import markup


@bot.message_handler(content_types=['new_chat_members'])
async def new_chat_members(message: Message):
    await bot.send_message(chat_id=message.chat.id, text=f"<b>Assalom alaykum <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>!</b>\n\n{message.chat.title} guruhiga xush kelibsiz.", reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['left_chat_member'])
async def left_chat_member(message: Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

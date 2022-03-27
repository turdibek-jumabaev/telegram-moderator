import datetime
import re
import asyncio
from loader import bot
from telebot.types import Message
from telebot.asyncio_filters import TextStartsFilter
import filters


@bot.message_handler(is_admin=True, text_startswith="!ro")
async def command_ro(message: Message):
    if message.reply_to_message:
        member = message.reply_to_message.from_user
        member_id = member.id
        chat_id = message.chat.id
        command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
        parsed = command_parse.match(message.text)
        time = parsed.group(2)
        comment = parsed.group(3)
        if not time:
            time = 5

        time = int(time)
        until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

        try:
            await bot.restrict_chat_member(chat_id, member_id, until_date=until_date, can_send_messages=False)
        except Exception as e:
            await bot.send_message(chat_id, f"<b>Error:</b> {e}")

        await bot.send_message(chat_id, f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time} minut yozish huquqidan mahrum qilindi.\n"
                               f"Sabab: \n<b>{comment}</b>")
    else:
        msg = await bot.reply_to(message=message, text="Cheklamoqchi bo'lgan foydalanuvchi xabariga javob qilib jo'nating...")

        await asyncio.sleep(10)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)


@bot.message_handler(is_admin=True, text_startswith="!unro")
async def command_unro(message: Message):
    if message.reply_to_message:
        member = message.reply_to_message.from_user
        member_id = member.id
        chat_id = message.chat.id

        try:
            await bot.restrict_chat_member(chat_id, member_id, until_date=None, can_send_messages=True)
        except Exception as e:
            await bot.send_message(chat_id, f"<b>Error:</b> {e}")

        await bot.send_message(chat_id, f"Foydalanuvchi {message.reply_to_message.from_user.full_name} cheklovdan ozod qilindi.")
    else:
        msg = await bot.reply_to(message=message, text="Ozod qilmoqchi bo'lgan foydalanuvchi xabariga javob qilib jo'nating...")

        await asyncio.sleep(10)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)

bot.add_custom_filter(filters.is_admin_filter.IsAdminFilter())
bot.add_custom_filter(TextStartsFilter())

from loader import bot
import telebot


class IsAdminFilter(telebot.asyncio_filters.SimpleCustomFilter):
    key = "is_admin"

    @staticmethod
    async def check(message: telebot.types.Message):
        result = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        return result.status == "administrator" or result.status == "creator"

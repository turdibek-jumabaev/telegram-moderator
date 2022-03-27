from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = [
    InlineKeyboardButton(
        text="Instagram", url="https://www.instagram.com/saidbekarislonov/"),
    InlineKeyboardButton(text="Telegram", url="https://t.me/Saidbekarislonov"),
    InlineKeyboardButton(
        text="Youtube", url="https://www.youtube.com/saidbekarislonov"),
    InlineKeyboardButton(
        text="Twitter", url="https://twitter.com/Saidbekarislonov"),
    InlineKeyboardButton(
        text="Facebook", url="https://www.facebook.com/SaidbekArs"),
    InlineKeyboardButton(text="Telegram", url="https://t.me/saidbekarislonov"),
    InlineKeyboardButton(
        text="Linkedin", url="https://www.linkedin.com/in/saidbekarislonov/"),
]

markup = InlineKeyboardMarkup(row_width=2).add(*buttons)

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = [
    InlineKeyboardButton(text='Silikon Vodiysi',
                         url="https://youtube.com/playlist?list=PLHNaMQIyrDHOq1tkc_KQXFlLariEonAJR"),
    InlineKeyboardButton(
        text='HTML va CSS', url="https://www.youtube.com/playlist?list=PLHNaMQIyrDHOZhHnc2UdQEOHrb1xM7HaF"),
    InlineKeyboardButton(text='JavaScript darsliklari',
                         url="https://www.youtube.com/playlist?list=PLHNaMQIyrDHPOSmeUz--1CWj0VW8h26LN"),
    InlineKeyboardButton(text='Website yaratish',
                         url="https://youtube.com/playlist?list=PLHNaMQIyrDHM8esvCO8s3ZbY-WVM4-KXT"),
    InlineKeyboardButton(
        text='Live Stream', url="https://www.youtube.com/playlist?list=PLHNaMQIyrDHOZhHnc2UdQEOHrb1xM7HaF"),
    InlineKeyboardButton(text='Sayohat va Vlog',
                         url="https://youtube.com/playlist?list=PLHNaMQIyrDHN2bVK0_JL8H_QhlI71jaxr"),
    InlineKeyboardButton(
        text='API, GitHub, JIRA, HOSTING va boshqalar', url="https://youtube.com/playlist?list=PLHNaMQIyrDHNN6XqrPquiaQwlAemp-dMU"),
]

markupStart = InlineKeyboardMarkup(row_width=2).add(*buttons)

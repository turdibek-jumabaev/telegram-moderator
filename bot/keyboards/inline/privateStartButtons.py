from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = [
    InlineKeyboardButton(text='Silikon Vodiysi', callback_data='silikon'),
    InlineKeyboardButton(text='HTML va CSS', callback_data='html_css'),
    InlineKeyboardButton(text='JavaScript darsliklari',
                         callback_data='javascript'),
    InlineKeyboardButton(text='Website yaratish', callback_data='website'),
    InlineKeyboardButton(text='Live Stream', callback_data='live_stream'),
    InlineKeyboardButton(text='Sayohat va Vlog', callback_data='sayohat_vlog'),
    InlineKeyboardButton(
        text='API, GitHub, JIRA, HOSTING va boshqalar', callback_data='api'),
]

markupStart = InlineKeyboardMarkup(row_width=2).add(*buttons)

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import choose_direction, menu

menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Помощь", callback_data=menu.new("need", "none")),
    ],
    [
        InlineKeyboardButton(text="Информация о стажировке", callback_data=menu.new("none", "information"))
    ]
])

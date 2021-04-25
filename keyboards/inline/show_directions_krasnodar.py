from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import choose_direction

directions_krasnodar = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Разработка", callback_data=choose_direction.new(name="development_krasnodar"))
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data=choose_direction.new(name="back_to_cities"))
    ]
])

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import choose_direction

directions_yekat = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Разработка", callback_data=choose_direction.new(name="development_yekat")),
        InlineKeyboardMarkup(text="Тестирование", callback_data=choose_direction.new(name="testing"))
    ],
    [
        InlineKeyboardButton(text="Аналитика", callback_data=choose_direction.new(name="analytics")),
        InlineKeyboardButton(text="Документация", callback_data=choose_direction.new(name="documentation"))
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data=choose_direction.new(name="back_to_cities"))
    ]
])

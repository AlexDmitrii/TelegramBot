from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import choose_city_callback, enter_anketa, cancel

enter_anketa = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Пройти анкету", callback_data=enter_anketa.new(anketa="enter"))
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data=cancel.new(value="back_to_direction"))
    ]
])

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import choose_city_callback, back

cities = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Екатеринбург",
                             callback_data=choose_city_callback.new(
                                 name="Екатеринбург",
                                 quantity=4,
                                 cancel="none")),
        InlineKeyboardButton(text="Краснодар",
                             callback_data=choose_city_callback.new(name="Краснодар", quantity=1, cancel="none")),
        InlineKeyboardButton(text="Челябинск",
                             callback_data=choose_city_callback.new(name="Челябинск", quantity=0, cancel="none")),
    ],
    [
        InlineKeyboardButton(text="Тверь",
                             callback_data=choose_city_callback.new(name="Тверь", quantity=0, cancel="none ")),
        InlineKeyboardButton(text="Санкт-Петербург",
                             callback_data=choose_city_callback.new(name="Санкт-Петербург", quantity=0, cancel="none"))
    ],
    [
        InlineKeyboardButton(text="Назад",
                             callback_data=back.new("back_to_main"))
    ]
])

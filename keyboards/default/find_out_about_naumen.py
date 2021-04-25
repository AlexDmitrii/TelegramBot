from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

find_out_about_naumen = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сайт компании"),
            KeyboardButton(text="Увидел рекламу в интернете"),
            KeyboardButton(text="На сайте hh.ru")
        ],
        [
            KeyboardButton(text="Участвовал в образовательных программах от компании"),
            KeyboardButton(text="Социальные сети"),
            KeyboardButton(text="От друзей или преподавателей")
        ],
        [
            KeyboardButton(text="Афишы и стенды в университете")
        ]
    ],
    resize_keyboard=True
)

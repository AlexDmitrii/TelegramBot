from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

education = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Высшее"),
            KeyboardButton(text="Незаконченное высшее")
        ],
        [
            KeyboardButton(text="Среднее профессиональное")
        ]
    ],
    resize_keyboard=True
)

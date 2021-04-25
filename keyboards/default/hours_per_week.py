from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

hours_per_week = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="40 часов (полный рабочий день)")
        ],
        [
            KeyboardButton(text="> 30 часов"),
            KeyboardButton(text="< 30 часов")
        ]
    ],
    resize_keyboard=True
)

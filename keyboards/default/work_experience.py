from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

work_experience = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅")
        ],
        [
            KeyboardButton(text="❌")
        ]
    ],
    resize_keyboard=True
)

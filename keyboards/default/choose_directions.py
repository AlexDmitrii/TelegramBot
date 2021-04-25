from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choose_directions = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Разработка"),
            KeyboardButton(text="Тестирование")
        ],
        [
            KeyboardButton(text="Аналитика"),
            KeyboardButton(text="Документация")
        ]
    ],
    resize_keyboard=True
)

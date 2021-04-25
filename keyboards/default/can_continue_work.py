from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

can_continue_work = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Нет, только на период стажировки"),
            KeyboardButton(text="Да, на полный рабочий день")
        ],
        [
            KeyboardButton(text="Да, на не полный рабочий день")
        ]
    ],
    resize_keyboard=True
)

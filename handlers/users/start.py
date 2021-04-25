from aiogram import types
from aiogram.types import Message
from loader import bot
from keyboards.inline.choose_city import cities
from keyboards.inline.menu import menu

from loader import dp


@dp.message_handler(commands=['start'], state="*")
async def hello(message: types.Message):
    print("Started!")
    await message.answer("Приветствую, будущий стажер!\n"
                         "Я бот Наумен и я буду тебя направлять на путь становления стажером нашей компании.\n"
                         )
    await message.answer("На стажировке тебя ждет:\n"
                         "👨‍💼 Опытный наставник и атмосфера поддержки\n"
                         "👨‍💻 Работа над реальными задачами\n"
                         "🚀Использование передовых технологий\n"
                         "🗒Удобный график работы\n"
                         "💰Стипендия\n"
                         "🏢Возможность попасть в штат компании\n"
                         "📈Профессиональное развитие\n"
                         "🎇Яркие корпоративы\n"
                         )
    await message.answer("Кого мы ждем:\n"
                         "Выпускников и студентов ИТ-специальностей, которые:\n"
                         "👉️ готовы работать не менее 30 часов в неделю\n"
                         "👉 обладают знаниями, соответствующими требованиям по выбранному направлению стажировки\n"
                         "👉 готовы выполнить тестовое задание и пройти собеседование\n"
                         "👉 умеют сдавать работу точно в срок\n"
                         "👉 могут найти общий язык с командой, не стесняются задавать уточняющие вопросы и просить помощи у коллег\n"
                         "👉 хотят развиваться в области ИТ\n")

    await message.answer("Этапы прохождения на стажировку!")
    photo = open("/home/dmitrii/TemplateTelegramBot/documents/steps.png", 'rb')
    await bot.send_photo(message.chat.id, photo)

    await message.answer("Меню.", reply_markup=menu)
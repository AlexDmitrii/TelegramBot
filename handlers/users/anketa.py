from aiogram import types
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as md
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ParseMode, ReplyKeyboardRemove, CallbackQuery
import re

from keyboards.default import work_experience
from loader import dp
from keyboards.default.hours_per_week import hours_per_week
from keyboards.default.can_continue_work import can_continue_work
from keyboards.default.education import education
from keyboards.default.find_out_about_naumen import find_out_about_naumen
from keyboards.default.choose_directions import choose_directions

# SERVICE_ACCOUNT_FILE = '/home/dmitrii/TemplateTelegramBot/handlers/users/key.json'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#
# creds = None
# creds = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#
# SAMPLE_SPREADSHEET_ID = '1mHujKDGeNAh4o6LmEUgyh0P3ZTP0l6qrdVSX5fVBSHU'
#
# service = build('sheets', 'v4', credentials=creds)
#
# # Call the Sheets API
# sheet = service.spreadsheets()


class Anketa(StatesGroup):
    direction = State()
    lastname = State()
    firstname = State()
    patronymic = State()
    date_of_birth = State()
    city = State()
    email = State()
    phone_number = State()
    hours_per_week = State()
    date_of_start = State()
    can_continue_work = State()
    education = State()
    name_of_institution = State()
    year_of_receipt = State()
    year_of_graduation = State()
    faculty = State()
    average_score = State()
    work_experience = State()
    period_of_work = State()
    place_of_work = State()
    post = State()
    duties = State()
    participation_in_projects = State()
    participation_in_educational_programs = State()
    main_skills = State()
    professional_interests = State()
    last_professional_book = State()
    hobby = State()
    result_of_practice = State()
    want_post = State()
    find_out_about_naumen = State()
    find_out_about_internship = State()
    recommendation = State()
    resume = State()
    test_task = State()
    confirm = State()


@dp.message_handler(state="*", commands=['cancel'])
@dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.answer("Заполнение анкеты отменено.")


@dp.callback_query_handler(text_contains="enter")
async def start_anketa(call: CallbackQuery):
    await Anketa.direction.set()
    await call.message.answer("Примечание: \n"
                              "🔻 - обязательно к ответу.\n"
                              "/cancel - отменить заполнение анкеты\n"
                              "Если не можете ответить или недостаточно информации для ответа, ставьте прочерк. (-)")
    await call.message.answer("🔻 Какое направление стажировки тебя интересует? ", reply_markup=choose_directions)


@dp.message_handler(state=Anketa.direction)
async def process_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text

    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())
    await Anketa.next()
    await message.answer("🔻 Фамилия:")


@dp.message_handler(state=Anketa.lastname)
async def process_lastname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lastname'] = message.text

    await Anketa.next()
    await message.answer("🔻 Имя:")


@dp.message_handler(state=Anketa.firstname)
async def process_firstname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['firstname'] = message.text

    await Anketa.next()
    await message.answer("🔻 Отчество:")


@dp.message_handler(state=Anketa.patronymic)
async def process_patronymic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text

    await Anketa.next()
    await message.answer("🔻 Дата рождения (формат: 07.12.1970)")


@dp.message_handler(state=Anketa.date_of_birth)
async def process_date_of_birth(message: types.Message, state: FSMContext):
    date_of_birth = message.text
    if not re.match(r"^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", date_of_birth):
        await message.answer("Введите верный формат даты. Пример: 07.12.1970")
        return

    async with state.proxy() as data:
        data['date_of_birth'] = message.text

    await Anketa.next()
    await message.answer("🔻 Город:")


@dp.message_handler(state=Anketa.city)
async def process_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = str(message.text)

    await Anketa.next()
    await message.answer("🔻 E-mail: ")


@dp.message_handler(state=Anketa.email)
async def process_email(message: types.Message, state: FSMContext):
    email = str(message.text)
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        await message.answer("Введите действительную почту. Пример: naumen@mail.ru")
        return

    async with state.proxy() as data:
        data['email'] = email

    await Anketa.next()
    await message.answer("Номер телефона (формат: +79123456789)")


@dp.message_handler(state=Anketa.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    if not re.match(r"^((\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", phone_number):
        await message.answer("Введите номер правильного формата. Пример: +79123456789")
        return

    async with state.proxy() as data:
        data['phone_number'] = phone_number

    await Anketa.next()
    await message.answer("🔻 Сколько часов в неделю сможешь уделять стажировке?", reply_markup=hours_per_week)


@dp.message_handler(state=Anketa.hours_per_week)
async def process_hours_per_week(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hours_per_week'] = message.text

    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())
    await Anketa.next()
    await message.answer("🔻 Когда сможешь приступить к стажировке? (Формат: 07.12.2021)")


@dp.message_handler(state=Anketa.date_of_start)
async def process_date_of_start(message: types.Message, state: FSMContext):
    date_of_start = message.text
    if not re.match(r"^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", date_of_start):
        await message.answer("Введите верный формат даты. Пример: 07.12.2021")
        return

    async with state.proxy() as data:
        data['date_of_start'] = message.text

    await Anketa.next()
    await message.answer("🔻 Сможешь продолжать работу после окончания стажировки?\n"
                         "Если нет подходящего варианта -> напишите свой.", reply_markup=can_continue_work)


@dp.message_handler(state=Anketa.can_continue_work)
async def process_can_continue_work(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['can_continue_work'] = message.text

    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())
    await Anketa.next()
    await message.answer("🔻 Образование.\n"
                         "Если нет подходящего варианта -> напишите свой:",
                         reply_markup=education)


@dp.message_handler(state=Anketa.education)
async def process_education(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['education'] = message.text

    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())
    await Anketa.next()
    await message.answer("🔻 Наименование учебного заведения:")


@dp.message_handler(state=Anketa.name_of_institution)
async def process_name_of_institution(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_of_institution'] = message.text

    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())
    await Anketa.next()
    await message.answer("🔻 Год поступления: ")


@dp.message_handler(state=Anketa.year_of_receipt)
async def process_year_of_receipt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year_of_receipt'] = message.text

    await Anketa.next()
    await message.answer("🔻 Год окончания: ")


@dp.message_handler(state=Anketa.year_of_graduation)
async def process_year_of_graduation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year_of_graduation'] = message.text

    await Anketa.next()
    await message.answer("🔻 Факультет, специальность: ")


@dp.message_handler(state=Anketa.faculty)
async def process_faculty(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['faculty'] = message.text

    await Anketa.next()
    await message.answer("🔻 Средний балл:")


@dp.message_handler(state=Anketa.average_score)
async def process_average_score(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['average_score'] = message.text

    await Anketa.next()
    await message.answer("Опыт работы: ", reply_markup=work_experience)


@dp.message_handler(state=Anketa.work_experience)
async def process_work_experience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['work_experience'] = message.text

        await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())
        await Anketa.next()
        await message.answer("Период работы с ... до ...")


@dp.message_handler(state=Anketa.period_of_work)
async def process_period_of_work(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['period_of_work'] = message.text

    await Anketa.next()
    await message.answer("Место работы: ")


@dp.message_handler(state=Anketa.place_of_work)
async def process_place_of_work(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['place_of_work'] = message.text

    await Anketa.next()
    await message.answer("Должность: ")


@dp.message_handler(state=Anketa.post)
async def process_post(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post'] = message.text

    await Anketa.next()
    await message.answer("Обязанности: ")


@dp.message_handler(state=Anketa.duties)
async def process_duties(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['duties'] = message.text

    await Anketa.next()
    await message.answer("В каких проектах ты принимал участие (включая учебные проекты): ")


@dp.message_handler(state=Anketa.participation_in_projects)
async def process_participation_in_projects(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['participation_in_projects'] = message.text

    await Anketa.next()
    await message.answer("Участвовал ли ты в образовательных программах от Naumen? \n"
                         "Если да - расскажи об этом подробнее: ")


@dp.message_handler(state=Anketa.participation_in_educational_programs)
async def process_participation_in_educational_programs(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['participation_in_educational_programs'] = message.text

    await Anketa.next()
    await message.answer("🔻 Ключевые навыки: ")


@dp.message_handler(state=Anketa.main_skills)
async def process_main_skills(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['main_skills'] = message.text

    await Anketa.next()
    await message.answer("🔻 Профессиональные интересы: ")


@dp.message_handler(state=Anketa.professional_interests)
async def process_professional_interests(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['professional_interests'] = message.text

    await Anketa.next()
    await message.answer("🔻 Последняя прочитанная профессиональная книга: ")


@dp.message_handler(state=Anketa.last_professional_book)
async def process_last_professional_boot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_professional_book'] = message.text

    await Anketa.next()
    await message.answer("🔻 Как ты проводишь свободное время? Чем увлекаешься? ")


@dp.message_handler(state=Anketa.hobby)
async def process_hobby(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = message.text

    await Anketa.next()
    await message.answer("🔻 Что даст тебе прохождение практики в нашей компании? ")


@dp.message_handler(state=Anketa.result_of_practice)
async def process_result_of_practice(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['result_of_practice'] = message.text

    await Anketa.next()
    await message.answer("🔻 Какую должность ты хочешь занять через 3-5 лет: ")


@dp.message_handler(state=Anketa.want_post)
async def process_want_post(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['want_post'] = message.text

    await Anketa.next()
    await message.answer("🔻 Как ты узнал о компании NAUMEN? ",
                         reply_markup=find_out_about_naumen)


@dp.message_handler(state=Anketa.find_out_about_naumen)
async def process_find_out_about_naumen(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['find_out_about_naumen'] = message.text

    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())
    await Anketa.next()
    await message.answer("🔻 Как ты узнал о стажировке в компании NAUMEN? ",
                         reply_markup=find_out_about_naumen)


@dp.message_handler(state=Anketa.find_out_about_internship)
async def process_find_out_about_internship(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['find_out_about_internship'] = message.text

    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())
    await Anketa.next()
    await message.answer("🔻 Кто может дать рекомендации? (ФИО, должность, телефон) ")


@dp.message_handler(state=Anketa.recommendation)
async def process_recommendation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['recommendation'] = message.text

    await Anketa.next()
    await message.answer("🔻 Ссылка на резюме: ")


@dp.message_handler(state=Anketa.resume)
async def process_resume(message: types.Message, state: FSMContext):
    resume = message.text
    if not re.match(
            r"^((ftp|http|https):\/\/)?(www\.)?([A-Za-zА-Яа-я0-9]{1}[A-Za-zА-Яа-я0-9\-]*\.?)*\.{1}[A-Za-zА-Яа-я0-9-]{2,8}"
            r"(\/([\w#!:.?+=&%@!\-\/])*)?",
            resume):
        await message.answer("Отправьте действительную ссылку на резюме. Попробуйе ещё раз")
        return

    async with state.proxy() as data:
        data['resume'] = message.text

    await Anketa.next()
    await message.answer("🔻 Ссылка на решенное тестовое задание: ")


@dp.message_handler(state=Anketa.test_task)
async def process_resume(message: types.Message, state: FSMContext):
    test_task = message.text
    if not re.match(
            r"^((ftp|http|https):\/\/)?(www\.)?([A-Za-zА-Яа-я0-9]{1}[A-Za-zА-Яа-я0-9\-]*\.?)*\.{1}[A-Za-zА-Яа-я0-9-]{2,8}"
            r"(\/([\w#!:.?+=&%@!\-\/])*)?",
            test_task):
        await message.answer("Отправьте действительную ссылку на решенное тестовое задание. Попробуйт ещё раз")
        return

    async with state.proxy() as data:
        data['test_task'] = message.text

    await Anketa.next()
    await message.answer(
        md.text(
            md.text("Ваша анкета, ", data['lastname']),
            md.text('Направление: ', data['direction']),
            md.text('Фамилия: ', data['lastname']),
            md.text('Имя: ', data['firstname']),
            md.text('Отчество: ', data['patronymic']),
            md.text('Дата рождения: ', data['date_of_birth']),
            md.text('Город: ', data['city']),
            md.text('E-mail: ', data['email']),
            md.text('Номер телефона: ', data['email']),
            md.text('Сколько часов в неделю сможешь уделять стажировке: ', data['hours_per_week']),
            md.text('Когда сможешь приступить к стажировке: ', data['date_of_start']),
            md.text('Сможешь продолжать работу после окончания стажировки: ', data['can_continue_work']),
            md.text("Образование: ", data['education']),
            md.text("Наименование учебного заведения: ", data['name_of_institution']),
            md.text("Год поступления: ", data['year_of_receipt']),
            md.text("Год выпуска: ", data['year_of_graduation']),
            md.text("Факультет, специальность: ", data['faculty']),
            md.text("Средние балл: ", data['average_score']),
            md.text("Опыт работы: ", data['work_experience']),
            md.text("Период работы с ... до ... : ", data['period_of_work']),
            md.text("Место работы: ", data['place_of_work']),
            md.text("Должность: ", data['post']),
            md.text("Обязанности: ", data['duties']),
            md.text("В каких проектах принимал участие (включая учебные проекты): ",
                    data['participation_in_projects']),
            md.text("Участвовал ли в образовательных программах от NAUMEN: ",
                    data['participation_in_educational_programs']),
            md.text("Ключевые навыки: ", data['main_skills']),
            md.text("Профессиональные интересы: ", data['professional_interests']),
            md.text("Последняя прочитанная профессиональная книга: ", data['last_professional_book']),
            md.text("Как ты проводишь свободное время? Чем увлекаешься? ", data['hobby']),
            md.text("Что даст тебе прохождение практики в нашей компании? ", data['result_of_practice']),
            md.text("Какую должность хочешь занять через 3-5 лет? ", data['want_post']),
            md.text("Как ты узнал о компании NAUMEN?", data['find_out_about_naumen']),
            md.text("Как ты узнал о стажировке в компании NAUMEN? ", data['find_out_about_internship']),
            md.text("Кто может дать тебе рекомендацию? ", data['recommendation']),
            md.text("Ссылка на резюме: ", data['resume']),
            md.text("Ссылка на решенное тестовое задание: ", data['test_task']),
            sep='\n',
        ),
        parse_mode=ParseMode.MARKDOWN
    )
    await message.answer("🔻 Напишите \"Да\" если данные верны: ")


@dp.message_handler(state=Anketa.confirm)
async def process_confirm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['confirm'] = message.text

    if data['confirm'] == "да".lower():
        result = []
        values = []
        for el in data.values():
            values.append(el)

        result.append(values)
        #
        # sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #                       range="Sheet2!A2", valueInputOption="RAW",
        #                       body={"values": result}).execute()
        # await state.finish()
        await message.answer("Анкета отправлена. :) ", parse_mode='Markdown')
    else:
        await state.finish()
        await message.answer("Анкетирование отменено.")

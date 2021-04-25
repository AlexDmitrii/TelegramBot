from aiogram.utils.callback_data import CallbackData

choose_city_callback = CallbackData("choose", "name", "quantity", "cancel")
enter_anketa = CallbackData("enter", "anketa")
menu = CallbackData("menu", "help", "information")
cancel = CallbackData("cancel", "value")
choose_direction = CallbackData("direction", "name")
back = CallbackData("back", "value")

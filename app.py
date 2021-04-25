from aiogram import executor


async def on_startup(dispatcher):
    # Уведомляет про запуск
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)

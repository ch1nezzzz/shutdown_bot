import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Отправьте команду /shutdown, чтобы выключить компьютер.')

async def shutdown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    await update.message.reply_text('Успешно, компьютер выключен.')
    print(f"Команда на выключение получена от пользователя: {user.username} ({user.id})")

    # Выполнение команды выключения
    if os.name == 'nt':  # Windows
        os.system('shutdown /s /t 1')
    else:  # Linux / macOS
        os.system('shutdown now')

def main():
    # Замените 'YOUR_BOT_TOKEN' на токен вашего Telegram-бота
    application = Application.builder().token('7671536175:AAGw4HfBCzFd4amfRB1ScRwKdpR1lLDCuLw').build()

    # Обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('shutdown', shutdown))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()

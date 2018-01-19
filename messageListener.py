import secrets
import telegram
import doorOpener
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler

def handleButtonCallback(bot, update):
    msg = update.callback_query.data
    if (msg == "open"):
        bot.sendMessage(secrets.chatId, text="Tür wird geöffnet")
        doorOpener.openDoor()

def handleOpenCommand(bot, update):
    bot.sendMessage(secrets.chatId, text="Tür wird geöffnet")
    doorOpener.openDoor()

def messageListener():
    print("Starting Telegram message listener...")
    updater = Updater(token=secrets.telegramToken)
    dispatcher = updater.dispatcher

    callback_handler = CallbackQueryHandler(handleButtonCallback)

    command_handler = CommandHandler("open", handleOpenCommand)

    dispatcher.add_handler(callback_handler)
    dispatcher.add_handler(command_handler)

    updater.start_polling()

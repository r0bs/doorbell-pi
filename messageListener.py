import secrets
import telegram
import doorOpener
from telegram.ext import Updater, CallbackQueryHandler

def handleButtonCallback(bot, update):
    msg = update.callback_query.data
    if (msg == "open"):
        doorOpener.openDoor()
        bot.sendMessage(secrets.chatId, text="Tür wird geöffnet")

def messageListener():
    print("Starting Telegram message listener...")
    updater = Updater(token=secrets.telegramToken)
    dispatcher = updater.dispatcher

    callback_handler = CallbackQueryHandler(handleButtonCallback)

    dispatcher.add_handler(callback_handler)

    updater.start_polling()

import secrets
import telegram
import doorOpener
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler

def handleButtonCallback(bot, update):
    msg = update.callback_query.data
    if (msg == "open"):
        print("Received callback instruction to open the door.")
        bot.sendMessage(secrets.chatId, text="Tür wird geöffnet")
        doorOpener.openDoor()

def handleOpenCommand(bot, update):
    print("Received message instruction to open the door.")
    bot.sendMessage(secrets.chatId, text="Tür wird geöffnet")
    doorOpener.openDoor()

def handleStartCommand(bot, update):
    print("Received start command.")
    bot.sendMessage(secrets.chatId, text="Hi! Send /open to open the door or wait for ring signal.")

def messageListener():
    print("Starting Telegram message listener...")
    updater = Updater(token=secrets.telegramToken)
    dispatcher = updater.dispatcher

    callback_handler = CallbackQueryHandler(handleButtonCallback)

    command_handler = CommandHandler("open", handleOpenCommand)

    dispatcher.add_handler(callback_handler)
    dispatcher.add_handler(command_handler)

    updater.start_polling()

import secrets
import telegram
import doorOpener
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler

def isAuthorized(chatId):
    return chatId in secrets.validChats
    print("Calling chatId isn't valid.")

def handleButtonCallback(bot, update):
    if(isAuthorized(update))
        msg = update.callback_query.data
        if (msg == "open"):
            print("Received callback instruction to open the door.")
            bot.sendMessage(secrets.chatId, text="Tür wird geöffnet")
            doorOpener.openDoor()

def handleOpenCommand(bot, update):
    if(isAuthorized(update))
        print("Received message instruction to open the door.")
        bot.sendMessage(secrets.chatId, text="Tür wird geöffnet")
        doorOpener.openDoor()

def handleStartCommand(bot, update):
    if(isAuthorized(update))
        print("Received start command.")
        bot.sendMessage(secrets.chatId, text="Hi! Send /open to open the door or wait for ring signal.")

def messageListener():
    print("Starting Telegram message listener...")
    updater = Updater(token=secrets.telegramToken)
    dispatcher = updater.dispatcher

    callback_handler = CallbackQueryHandler(handleButtonCallback)

    start_command_handler = CommandHandler("start", handleStartCommand)
    open_command_handler = CommandHandler("open", handleOpenCommand)

    dispatcher.add_handler(callback_handler)
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(open_command_handler)

    updater.start_polling()

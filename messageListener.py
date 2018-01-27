import secrets
import telegram
import notifier
import doorOpener
import buzzer
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler

def isAuthorized(chatId):
    isValid = str(chatId) in secrets.validChats
    if(isValid):
        return True
    else:
        print("Calling chatId" + chatIdchatId + "isn't valid.")

def handleButtonCallback(bot, update):
    if(isAuthorized(update.callback_query.message.chat.id)):
        msg = update.callback_query.data
        if (msg == "open"):
            print("Received callback instruction to open the door.")
            bot.sendMessage(secrets.chatId, text="Door is opening.")
            doorOpener.openDoor()

def handleOpenCommand(bot, update):
    if(isAuthorized(update.message.chat.id)):
        print("Received message instruction to open the door.")
        bot.sendMessage(secrets.chatId, text="Door is opening.")
        doorOpener.openDoor()

def handleStartCommand(bot, update):
    if(isAuthorized(update.message.chat.id)):
        print("Received start command.")
        bot.sendMessage(secrets.chatId, text="Hi! Send /open to open the door or wait for ring signal.")

def handleRingCommand(bot, update):
    if(isAuthorized(update.message.chat.id)):
        print("Received sound command.")
        bot.sendMessage(secrets.chatId, text="Beep! Beep! Beep!")
        buzzer.buzz()

def messageListener():
    print("Starting Telegram message listener...")
    updater = Updater(token=secrets.telegramToken)
    dispatcher = updater.dispatcher

    callback_handler = CallbackQueryHandler(handleButtonCallback)

    start_command_handler = CommandHandler("start", handleStartCommand)
    open_command_handler = CommandHandler("open", handleOpenCommand)
    ring_command_handler = CommandHandler("ring", handleRingCommand)

    dispatcher.add_handler(callback_handler)
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(open_command_handler)
    dispatcher.add_handler(ring_command_handler)

    updater.start_polling()
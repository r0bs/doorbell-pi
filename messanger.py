import secrets
import time
import logging
import telegram
import doorOpener
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def handleCallback(bot, update):
    msg = update.callback_query.data
    if (msg == "open"):
        doorOpener.openDoor()
        bot.sendMessage(secrets.chatId, text="Tür wird geöffnet")

def messageListener():
    print("Starting message listener...")
    updater = Updater(token=secrets.telegramToken)
    dispatcher = updater.dispatcher
    msg_open_handler = CommandHandler('/open', open)
    callback_handler = CallbackQueryHandler(handleCallback)
    dispatcher.add_handler(msg_open_handler)
    dispatcher.add_handler(callback_handler)
    updater.start_polling()

messageListener()

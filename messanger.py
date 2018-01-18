import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import secrets
import time
import logging




    
def composeMessage():
    host = "http://raspberrypi:9000/"
    messageText = "Ring! Ring! Open: "
    
    url = host 

    message = messageText + url
    return "Es hat an der Tür geklingelt"

def yolo(bot, update):
    print(update.callback_query.data)
    sendNotification()

def sendNotification():
    keyboard = [[InlineKeyboardButton("Öffnen", callback_data='open')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot = telegram.Bot(token=secrets.telegramToken)
    message = composeMessage()

    bot.sendMessage(secrets.chatId, text=message, reply_markup=reply_markup)

sendNotification()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=secrets.telegramToken)
dispatcher = updater.dispatcher
start_handler = CommandHandler('1', yolo)
callback_handler = CallbackQueryHandler(yolo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(callback_handler)
updater.start_polling()
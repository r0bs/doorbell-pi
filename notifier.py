import secrets
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def sendNotification():
    print("Sending notification to chat #" + secrets.chatId)

    bot = telegram.Bot(token=secrets.telegramToken)

    message = "Doorbell rings."
    keyboard = [[InlineKeyboardButton("Open", callback_data='open')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.sendMessage(secrets.chatId, text=message, reply_markup=reply_markup)
import secrets
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Notifier:

    # def __init__(self, tokenHandler):
    #     self.tokenHandler = tokenHandler

    # def getTokenAsString(self):
    #     return self.tokenHandler.generateToken().decode("utf-8")
    
    # def composeMessage(self):
    #     host = "http://raspberrypi:9000/"
    #     messageText = "Ring! Ring! Open: "
        
    #     token = self.getTokenAsString()
    #     url = host + token

    #     message = messageText + url
    #     return message

    def sendNotification():
        print("Sending notification to chat #" + secrets.chatId)

        bot = telegram.Bot(token=secrets.telegramToken)

        message = "Es hat geklingelt."
        keyboard = [[InlineKeyboardButton("Öffnen", callback_data='open')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        bot.sendMessage(secrets.chatId, text=message, reply_markup=reply_markup)
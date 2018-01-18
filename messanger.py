import telegram
import secrets
import time
    
def composeMessage():
    host = "http://raspberrypi:9000/"
    messageText = "Ring! Ring! Open: "
    
    url = host 

    message = messageText + url
    return message

def sendNotification():
    bot = telegram.Bot(token=secrets.telegramToken)
    message = composeMessage()

    localtime = time.asctime( time.localtime(time.time()) )

    print("Doorbell rang on: " + localtime + ". Sending notification to" + secrets.chatId)
    bot.sendMessage(secrets.chatId, message)

sendNotification()
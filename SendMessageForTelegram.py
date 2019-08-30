import telegram as tg

TelegramAPIToken = "837595101:AAFo68OQPvM8bq-zbF1xNDUHbf86fAuRb-I"

chatId = "964216246"

bot = tg.Bot(token = TelegramAPIToken)
updates = bot.getUpdates()

for msg in updates:
    print(msg.message)

bot.sendMessage(chatId, "hello i'm Bot")

bot.sendMessage(chatId, "Nice to meet you")

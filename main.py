import os

from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters


def start(bot,update):
    update.message.reply_text("Olá, esse bot foi feito para spammar o orgulho dasiano! Digite /dasi.", quote=False)


def dasi(bot, update):
    update.message.reply_text("GRIIIIIIIIIIFO", quote=False)
    update.message.reply_text("GRIFO GRIFO GRIFO", quote=False)
    update.message.reply_text("É DASI USP!", quote=False)


def webhook(request):
    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
    dispatcher = Dispatcher(bot, None, 0)
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("dasi", dasi))

    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return "ok"

import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("👋 Hello! I’m your AI Resume Bot. Type /resume to get started.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

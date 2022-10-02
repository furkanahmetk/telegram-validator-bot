import constants as constants
from telegram.ext import *
import handlers

print("Bot started")

def main():
    updater = Updater(constants.BOT_API_KEY, use_context= True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", handlers.start_command))
    dp.add_handler(CommandHandler("signin", handlers.get_public_key))

    dp.add_handler(MessageHandler(Filters.text, handlers.handle_message))

    dp.add_error_handler(handlers.error)

    updater.start_polling()

    updater.idle()

main()

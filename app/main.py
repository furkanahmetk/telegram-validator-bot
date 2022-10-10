import constants as constants
from telegram.ext import *
import handlers


print("Bot started")

def main():
    updater = Updater(constants.BOT_API_KEY, use_context= True)


    job_queue = JobQueue()
    dp = updater.dispatcher
    job_queue.set_dispatcher(dp)


    dp.add_handler(CommandHandler("start", handlers.start_command))
    dp.add_handler(CommandHandler("status", handlers.status))
    dp.add_handler(CommandHandler("totaldelegators", handlers.totaldelegators))
    dp.add_handler(CommandHandler("totalstake", handlers.totalstake))
    dp.add_handler(CommandHandler("fee", handlers.fee))
    dp.add_handler(CommandHandler("start_timer", handlers.start_timer, pass_job_queue=True))

    dp.add_handler(MessageHandler(Filters.text, handlers.handle_message))

    dp.add_error_handler(handlers.error)

    

    updater.start_polling()
    job_queue.start()

    updater.idle()

main()

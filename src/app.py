from platform import mac_ver, machine
from re import M
from telegram.ext import *
from src.service.bot_service import Bot_Service
import src.constants as constants
import os
from src.factory import database
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes


def create_app():
    load_dotenv()
    updater = Updater(os.environ.get("BOT_API_KEY"), use_context= True)


    job_queue = JobQueue()
    dp = updater.dispatcher
    job_queue.set_dispatcher(dp)

    bot_service = Bot_Service(updater)


    dp.add_handler(CommandHandler("start", bot_service.start_command))
    dp.add_handler(CommandHandler("status", bot_service.status))
    dp.add_handler(CommandHandler("totaldelegators", bot_service.total_delegators))
    dp.add_handler(CommandHandler("totalstake", bot_service.total_stake))
    dp.add_handler(CommandHandler("fee", bot_service.fee))
    dp.add_handler(CommandHandler("update", bot_service.update_me))
    dp.add_handler(CommandHandler("alarm", bot_service.alarm_me))
    dp.add_handler(CommandHandler("forget", bot_service.forget_validator))
    #dp.add_handler(CommandHandler("start_timer", bot_service.start_timer, pass_job_queue=True))

    #dp.add_handler(MessageHandler(Filters.text, bot_service.handle_message))

    dp.add_error_handler(bot_service.error)

    database.Database.init(constants.MONGO_URI,constants.DB_NAME)
    return updater,job_queue
    

    

def start_app(updater,job_queue):
    updater.start_polling()
    job_queue.start()
    updater.idle()

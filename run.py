from src.app import create_app,start_app
from flask_apscheduler import APScheduler
from src.service.repeated_tasks import Repeated_Task
from src.config import ProdConfig
updater,job_queue = create_app(config=ProdConfig)

#Start application, before starting flask application it configures and runs cron job to retrieve data
if __name__ == '__main__':
    scheduler = APScheduler()
    task = Repeated_Task(updater,ProdConfig)
    scheduler.add_job(id = '1', func = task.data_cron, trigger = 'interval', seconds = 30)
    scheduler.add_job(id = '2', func = task.alarm_cron, trigger = 'interval', seconds = 2*60)
    scheduler.add_job(id = '3', func = task.update_cron, trigger = 'interval', seconds =  30*60)
    scheduler.start()
    start_app(updater,job_queue)

  
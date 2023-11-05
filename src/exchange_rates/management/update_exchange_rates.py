from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from src.exchange_rates.management.commands.update_currency import Command

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

scheduler.add_job(Command().handle(), trigger="cron", hour=0)

scheduler.start()

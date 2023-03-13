from datetime import date
from fastapi_scheduler import SchedulerAdmin
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite

site = AdminSite(settings=Settings(database_url_async='sqlite+aiosqlite:///amisadmin.db'))

scheduler = SchedulerAdmin.bind(site)

@scheduler.scheduled_job('interval', seconds=60)
def interval_task_test():
    print('interval task is run...')

@scheduler.scheduled_job('cron', hour=3, minute=30)
def cron_task_test():
    print('cron task is run...')

@scheduler.scheduled_job('date', run_date=date(2023, 11, 11))
def date_task_test():
    print('date task is run...')
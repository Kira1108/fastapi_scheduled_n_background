# Background Task and Scheduled Task

## 1. Scheduled Task

`main.py`
```python
...
# for schedulled tasks you need this import
from scheduled_tasks import site, scheduler
...


@app.on_event("startup")
async def startup():
    # for schedulled tasks, you need this 2 lines
    site.mount_app(app)
    scheduler.start()

...
```

Defind a job by adding a function decorated with `@scheduler.scheduled_job`.    
`scheduled_tasks/tasks.py`
```python
from datetime import date
from fastapi_scheduler import SchedulerAdmin
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite

site = AdminSite(settings=Settings(database_url='sqlite:///amisadmin.db'))

scheduler = SchedulerAdmin.bind(site)

# Every 60 seconds, run the task
@scheduler.scheduled_job('interval', seconds=60)
def interval_task_test():
    print('interval task is run...')
```

## 2. Background Task
```python
from fastapi import BackgroundTasks

def sleep_task():
    time.sleep(3)
    print("Finished background tasks")
    
@app.get("/background")
def back(background_tasks: BackgroundTasks):
    # background_tasks is a dependency, like a self trigged 
    # list of tasks.
    
    # add a function to background_tasks
    background_tasks.add_task(sleep_task)
    return {'message':'background task is running'}
```

## 3. Copy requirements
`requirements.txt`
```bash
fastapi
uvicorn
python-multipart
aiosqlite
fastapi-scheduler
apscheduler
fastapi_amis_admin
```
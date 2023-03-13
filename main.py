from fastapi import FastAPI
from fastapi import BackgroundTasks

# for schedulled tasks you need this import
from scheduled_tasks import site, scheduler
import time

app = FastAPI()

@app.on_event("startup")
async def startup():
    # for schedulled tasks, you need this 2 lines
    site.mount_app(app)
    scheduler.start()
    
@app.get("/")
def ping():
    return {'message':'pong'}


def sleep_task():
    time.sleep(3)
    print("Finished background tasks")
    
@app.get("/background")
def back(background_tasks: BackgroundTasks):
    # background_tasks is a dependency.
    
    # add a function to background_tasks
    background_tasks.add_task(sleep_task)
    return {'message':'background task is running'}


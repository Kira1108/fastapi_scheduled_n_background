from fastapi import FastAPI
from fastapi import BackgroundTasks
from scheduled_tasks import site, scheduler
import time

app = FastAPI()

# copy this function, just copy, you don't have to understand 
# what happens here.
@app.on_event("startup")
async def startup():
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
    background_tasks.add_task(sleep_task)
    return {'message':'background task is running'}


from fastapi import FastAPI
from scheduled_tasks import site, scheduler

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
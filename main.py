from fastapi import FastAPI
from controller.test_controller import router as test_router
from controller.order_controller import router as order_router
from repository.database import database

app = FastAPI()
app.include_router(test_router)
app.include_router(order_router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
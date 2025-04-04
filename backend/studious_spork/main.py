from decouple import config

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from motor.motor_asyncio import AsyncIOMotorClient

from studious_spork.routers.cars import router as cars_router


DB_URL = config("DB_URL", cast=str)
DB_NAME = config("DB_NAME", cast=str)


# define origins
origins = ["*"]

# instantiate the app
app = FastAPI()

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(DB_URL)
    app.mongodb = app.mongodb_client.get_database("carsApp")
    app.collection = app.mongodb.get_collection("cars1")


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(cars_router, prefix="/cars", tags=["cars"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
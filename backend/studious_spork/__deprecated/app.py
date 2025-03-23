from typing import Dict

from fastapi import FastAPI, Body

import sys

from enum import Enum
from fastapi import FastAPI, Path
from pydantic import BaseModel

print(sys.executable)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world!"}


@app.post("/")
async def post_root():
    return {"message": "Post request success"}


@app.get("/car/{id}")
async def root(id: int):
    return {"car_id": id}


@app.get("/user/{id}")
async def user(id: int):
    return {"User_id": id}


@app.get("/user/me")
async def user():
    return {"User_id": "This is me!"}


app = FastAPI()


class AccountType(str, Enum):
    PRO = "pro"
    FREE = "free"


@app.get("/account/{acc_type}/{months}")
async def account(acc_type: AccountType, months: int = Path(..., ge=3, le=12)):
    return {"message": "Account created", "account_type": acc_type, "months": months}


@app.get("/cars/price")
async def cars_by_price(min_price: int = 0, max_price: int = 100000):
    return {"Message": f"Listing cars with prices between {min_price} and {max_price}"}


class InsertCar(BaseModel):
    brand: str
    model: str
    year: int


class InsertUser(BaseModel):
    username: str
    name: str


@app.post("/cars")
async def new_car(data: InsertCar = Body(...)):
    print(data)
    return {"message": data}


@app.post("/car/user")
async def new_car_model(
    car: InsertCar,
    user: InsertUser,
    code: int=Body(None) ):
    return {
        "car":car,
        "user":user,
        "code":code
    }
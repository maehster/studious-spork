import asyncio
from typing import Any

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from typing_extensions import Annotated





async def tmp():

    mongodb_client = AsyncIOMotorClient("mongodb+srv://compass:7p4wJb6ZBBozbynn@studious-spork.7xz88.mongodb.net/?retryWrites=true&w=majority&appName=studious-spork")
    mongodb = mongodb_client["carsApp"]

    result = await mongodb["cars1"].insert_one(
        jsonable_encoder(Model(id=ObjectId()))
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(tmp())
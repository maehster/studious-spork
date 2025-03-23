import asyncio
from typing import Optional

from beanie import PydanticObjectId
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field, BeforeValidator, ConfigDict
from typing_extensions import Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]


class Model(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class CarBase(Model):
    brand: str = Field(..., min_length=3)
    make: str = Field(..., min_length=3)
    year: int = Field(..., gt=1975, lt=2023)
    price: int = Field(...)
    km: int = Field(...)
    cm3: int = Field(...)

async def tmp():

    mongodb_client = AsyncIOMotorClient("mongodb+srv://compass:7p4wJb6ZBBozbynn@studious-spork.7xz88.mongodb.net/?retryWrites=true&w=majority&appName=studious-spork")
    mongodb = mongodb_client["carsApp"]

    result = await mongodb["cars1"].insert_one(
        CarBase(
            brand="aaa",
            make="bbb",
            year=2021,
            price=1,
            cm3=2,
            km=3
        ).model_dump(by_alias=True, exclude=["id"])
    )

    result = await mongodb["cars1"].find_one({"_id": ObjectId("67e0526ce7e080960cfe6ada")})
    print(result)


if __name__ == "__main__":
    asyncio.run(tmp())
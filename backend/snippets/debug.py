import asyncio
from typing import Any

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from typing_extensions import Annotated


class ObjectIdPydanticAnnotation:
    @classmethod
    def validate_object_id(cls, v: Any, handler) -> ObjectId:
        if isinstance(v, ObjectId):
            return v

        s = handler(v)
        if ObjectId.is_valid(s):
            return ObjectId(s)
        else:
            raise ValueError("Invalid ObjectId")

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, _handler) -> core_schema.CoreSchema:
        assert source_type is ObjectId
        return core_schema.no_info_wrap_validator_function(
            cls.validate_object_id,
            core_schema.str_schema(),
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def __get_pydantic_json_schema__(cls, _core_schema, handler) -> JsonSchemaValue:
        return handler(core_schema.str_schema())




class Model(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation]


async def tmp():

    mongodb_client = AsyncIOMotorClient("mongodb+srv://compass:7p4wJb6ZBBozbynn@studious-spork.7xz88.mongodb.net/?retryWrites=true&w=majority&appName=studious-spork")
    mongodb = mongodb_client["carsApp"]

    result = await mongodb["cars1"].insert_one(
        jsonable_encoder(Model(id=ObjectId()))
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(tmp())
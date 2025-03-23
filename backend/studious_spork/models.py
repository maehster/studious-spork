from bson import ObjectId
from pydantic import Field, BaseModel, AfterValidator, PlainSerializer, WithJsonSchema
from typing import Optional, Any, Annotated, Union

from pydantic_core import core_schema


class PyObjectId(str):
    # see here: https://stackoverflow.com/questions/76686888/using-bson-objectid-in-pydantic-v2/76837550#76837550

    @classmethod
    def __get_pydantic_core_schema__(
            cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(ObjectId),
                core_schema.chain_schema([
                    core_schema.str_schema(),
                    core_schema.no_info_plain_validator_function(cls.validate),
                ])
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x),
                when_used="json"
            ),
        )

    @classmethod
    def validate(cls, value) -> ObjectId:
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")

        return ObjectId(value)

class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}


class CarBase(MongoBaseModel):

    brand: str = Field(..., min_length=3)
    make: str = Field(..., min_length=3)
    year: int = Field(..., gt=1975, lt=2023)
    price: int = Field(...)
    km: int = Field(...)
    cm3: int = Field(...)


class CarUpdate(MongoBaseModel):
    price: Optional[int] = None


class CarDB(CarBase):
    pass

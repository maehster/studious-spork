from bson import ObjectId
from pydantic import Field, BaseModel, AfterValidator, PlainSerializer, WithJsonSchema
from typing import Optional, Any, Annotated, Union

from pydantic_core import core_schema


from typing_extensions import Annotated
from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator
from bson import ObjectId as _ObjectId


def check_object_id(value: str) -> str:
    if not _ObjectId.is_valid(value):
        raise ValueError('Invalid ObjectId')
    return value


ObjectId = Annotated[str, AfterValidator(check_object_id)]


class MongoBaseModel(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")



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

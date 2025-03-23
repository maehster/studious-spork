from bson import ObjectId
from pydantic import Field, BaseModel, AfterValidator, PlainSerializer, WithJsonSchema
from typing import Optional, Any, Annotated, Union

from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema


from typing_extensions import Annotated
from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator
from bson import ObjectId as _ObjectId


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


class CarBase(BaseModel):
    brand: str = Field(..., min_length=3)
    make: str = Field(..., min_length=3)
    year: int = Field(..., gt=1975, lt=2023)
    price: int = Field(...)
    km: int = Field(...)
    cm3: int = Field(...)


class CarUpdate(BaseModel):
    price: Optional[int] = None


class CarDB(CarBase):
    pass

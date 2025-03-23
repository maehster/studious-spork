from pydantic import Field, BeforeValidator, ConfigDict
from typing import Optional, Annotated
from pydantic import BaseModel


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


class CarUpdate(Model):
    price: Optional[int] = None


class CarDB(CarBase):
    pass

from enum import Enum
from typing import List
from pydantic import BaseModel, ValidationError


class Fuel(str, Enum):
    PETROL = "PETROL"
    DIESEL = "DIESEL"
    LPG = "LPG"


class Car(BaseModel):
    brand: str
    model: str
    year: int
    fuel: Fuel
    countries: List[str]
    note: str = "No note"

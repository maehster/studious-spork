from studious_spork.models import CarDB, CarBase, PyObjectId

car = {
    "_id": "test",
    "brand": "aaa",
    "make": "500",
    "year": 2015,
    "cm3": 1222,
    "price": 2000,
    "km": 100000
}

db = CarBase(
    _id=PyObjectId(),
    cm3=1,
    km=2,
    year=2000,
    make="ford",
    brand="ford",
    price=1,
)
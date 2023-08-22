from typing import Optional

from pydantic import BaseModel


class Events(BaseModel):
    pass


class Property(Events):
    id: Optional[str]
    name: str
    address: str
    price: float
    images: str


class User(Events):
    phone: str
    email: str
    photo: str

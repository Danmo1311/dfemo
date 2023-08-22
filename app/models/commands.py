from pydantic import BaseModel


class Command(BaseModel):
    pass


class Property(Command):
    name: str
    address: str
    price: float
    images: str


class User(Command):
    phone: str
    email: str
    photo: str

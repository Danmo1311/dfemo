from typing import List

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from models import commands
from services import handlers

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API de búsqueda a un click!"}


@app.get("/properties")
def properties():
    try:
        response = handlers.get_properties()
        return response

    except Exception as e:
        raise e


@app.get("/properties/{property_id}")
def property(property_id: str):
    response = handlers.get_property(property_id)
    return response


@app.post("/properties")
def property(property: List[commands.Property]):
    try:
        response = handlers.create_properties(property)
        return response
    except Exception as e:
        raise e


@app.put("/properties/{property_id}")
def property(property_id: str, property: commands.Property):
    handlers.update_property(property_id=property_id, property=property)
    return {"message": f"Actualizando la propiedad {property_id}"}


@app.delete("/properties/{property_id}")
def property(property_id: str):
    handlers.delete_property(property_id)
    return {"message": f"Eliminando la propiedad {property_id}"}


@app.get("/users")
def users():
    response = handlers.users()

    return response


@app.get("/users/{user_id}")
def user(user_id: str):
    response = handlers.get_user(user_id)
    return response


@app.post("/users")
def create_user(user: commands.User):
    handlers.create_user(user=user)
    return {"message": "Creando un nuevo usuario"}


@app.put("/users/{user_id}")
def update_user(user_id: str, user: commands.User):
    _ = handlers.update_user(user_id=user_id, user=user)
    return {"message": f"Actualizando el usuario {user_id}"}


@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    _ = handlers.delete_user(user_id=user_id)

    return {"message": f"Eliminando el usuario {user_id}"}

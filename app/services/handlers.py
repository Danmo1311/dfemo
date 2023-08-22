from typing import List

from bson import ObjectId
from pymongo import InsertOne

from config.database import db
from models import commands, events


def convert_to_json(data):
    all_properties = []
    for item in data:
        property = events.Property(
            # id=str(item["_id"]),
            name=item["name"],
            address=item["address"],
            price=item["price"],
            images=item["images"]
        )
        all_properties.append(property)
    return all_properties


def convert_to_json_user(data):
    all_users = []
    for item in data:
        user = events.User(
            user_id=str(item["_id"]),
            phone=item["phone"],
            email=item["email"],
            photo=item["photo"]

        )
        all_users.append(user)
    return all_users


def get_properties():
    col = db["properties"]

    try:
        response = col.find({})
        data = convert_to_json(response)
        return data

    except Exception as e:
        return {"message": "Error retrieving properties: " + str(e)}


def create_properties(properties: List[commands.Property]):
    col = db["properties"]

    bulk_operations = []
    for item in properties:
        operation = InsertOne({
            "name": item.name,
            "address": item.address,
            "price": item.price,
            "images": item.images
        })
        bulk_operations.append(operation)

    try:
        _ids = col.bulk_write(bulk_operations).upserted_ids
        return \
            {
                "message": "Properties created successfully",
                "ids": _ids.values()
            }

    except Exception as e:
        return {"message": "Error creating properties: " + str(e)}


def get_property(property_id):
    col = db["properties"]
    if not ObjectId.is_valid(property_id):
        return {"message": "Invalid property id"}
    try:
        response = col.find_one({"_id": ObjectId(property_id)})
        if response is None:
            return {"message": "Property not found"}
        data = events.Property(
            id=str(response["_id"]),
            name=response["name"],
            address=response["address"],
            price=response["price"],
            images=response["images"]
        )
        return data
    except Exception as e:
        raise {"message": "Error retrieving property: " + str(e)}


def update_property(property_id, property: commands.Property):
    col = db["properties"]
    if not ObjectId.is_valid(property_id):
        return {"message": "Invalid property id"}
    try:
        response = col.update_one({"_id": ObjectId(property_id)}, {"$set": {
            "name": property.name,
            "address": property.address,
            "price": property.price,
            "images": property.images
        }})
        if response.modified_count == 0:
            return {"message": "Property not found"}
        return {"message": "Property updated successfully"}
    except Exception as e:
        return {"message": "Error updating property: " + str(e)}


def delete_property(property_id):
    col = db["properties"]
    if not ObjectId.is_valid(property_id):
        return {"message": "Invalid property id"}
    try:
        response = col.delete_one({"_id": ObjectId(property_id)})
        if response.deleted_count == 0:
            return {"message": "Property not found"}
        return {"message": "Property deleted successfully"}
    except Exception as e:
        return {"message": "Error deleting property: " + str(e)}


def users():
    col = db["users"]

    try:
        response = col.find({})
        data = convert_to_json_user(response)
        return data

    except Exception as e:
        return {"message": "Error retrieving users: " + str(e)}


def get_user(user_id):
    col = db["users"]
    if not ObjectId.is_valid(user_id):
        return {"message": "Invalid user id"}
    try:
        response = col.find_one({"_id": ObjectId(user_id)})
        if response is None:
            return {"message": "User not found"}
        data = events.User(
            user_id=str(response["_id"]),
            phone=response["phone"],
            email=response["email"],
            photo=response["photo"]
        )
        return data
    except Exception as e:
        return {"message": "Error retrieving user: " + str(e)}


def create_user(user):
    col = db["users"]

    try:
        response = col.insert_one({
            "name": user.name,
            "email": user.email,
            "password": user.password
        })
        return {"message": "User created successfully"}

    except Exception as e:
        return {"message": "Error creating user: " + str(e)}


def update_user(user_id, user):
    col = db["users"]
    if not ObjectId.is_valid(user_id):
        return {"message": "Invalid user id"}
    try:
        response = col.update_one({"_id": ObjectId(user_id)}, {"$set": {
            "name": user.name,
            "email": user.email,
            "password": user.password
        }})
        if response.modified_count == 0:
            return {"message": "User not found"}
        return {"message": "User updated successfully"}
    except Exception as e:
        return {"message": "Error updating user: " + str(e)}


def delete_user(user_id):
    col = db["users"]
    if not ObjectId.is_valid(user_id):
        return {"message": "Invalid user id"}
    try:
        response = col.delete_one({"_id": ObjectId(user_id)})
        if response.deleted_count == 0:
            return {"message": "User not found"}
        return {"message": "User deleted successfully"}
    except Exception as e:
        return {"message": "Error deleting user: " + str(e)}

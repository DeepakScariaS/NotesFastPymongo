from fastapi import APIRouter

from models.notes import Note

from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


# GET Request Method
@router.get("/")
async def get_notes():
    notes = list_serial(collection_name.find())
    return notes


# POST
@router.post("/")
async def post_notes(note: Note):
    collection_name.insert_one(dict(note))


# PUT
@router.put("/{id}")
async def put_notes(id: str, note: Note):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(note)})


# DELETE
@router.delete("/{id}")
async def delete_notes(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})

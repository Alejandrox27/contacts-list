from fastapi import APIRouter, status, HTTPException
from models.contact import Contact
from db.database import engine

root = APIRouter(prefix="/contacts",
                 tags=["contacts"],
                 responses={404: {status.HTTP_404_NOT_FOUND: "Contact not found"}})
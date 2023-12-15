from fastapi import APIRouter, status, HTTPException
from models.contact import Contact
from db.database import engine
from schema.contacts import contacts
from models.contact import Contact

root = APIRouter(prefix="/contacts",
                 tags=["contacts"],
                 responses={404: {status.HTTP_404_NOT_FOUND: "Contact not found"}})

@root.get("/", response_model=list, status_code=status.HTTP_200_OK)
async def get_contacts():
    with engine.connect() as conn:
        contacts_list = conn.execute(contacts.select()).fetchall()
        columns = contacts.columns.keys()
        contacts_dict = [dict(zip(columns, contact)) for contact in contacts_list]
        
        return contacts_dict
    
@root.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def post_contact(contact: Contact):
    with engine.connect() as conn:
        contact_dict = contact.dict()
        contact_dict["id"] = None
        id = conn.execute(contacts.insert().values(contact_dict)).lastrowid
        conn.commit()
        
        result = conn.execute(contacts.select().where(contacts.c.id == id)).first()
        columns = contacts.columns.keys()
        
        if result:
            result = dict(zip(columns, result))
            return result
        return {'response': status.HTTP_404_NOT_FOUND}
    
@root.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(id: int):
    with engine.connect() as conn:
        conn.execute(contacts.delete().where(contacts.c.id == id))
        conn.commit()
from pydantic import BaseModel

class Contact(BaseModel):
    id: int | None = None
    name: str
    email: str
    phone: int
    
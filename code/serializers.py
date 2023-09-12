from pydantic import BaseModel

class Cat(BaseModel):
    name: str
    color: str
    image: str

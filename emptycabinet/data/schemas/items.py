from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

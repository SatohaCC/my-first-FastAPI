from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from typing import Union

router = APIRouter()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@router.post("/tutorial_body/")
async def create_item(item: Item):
    return item

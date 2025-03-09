from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import Optional

# Here the app variable will be an "instance" of the class FastAPI.
app = FastAPI()

from app.routers import tutorial_query_params
from app.routers import tutorial_body

app.include_router(tutorial_query_params.router)
app.include_router(tutorial_body.router)


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {"message": "Hello World"}

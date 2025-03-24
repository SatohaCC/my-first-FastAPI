from typing import Annotated, Literal

from fastapi import APIRouter, FastAPI, Query
from pydantic import BaseModel, Field


router = APIRouter()


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@router.get("/tutorial_query_param_models/")
async def read_items(
    filter_query: Annotated[FilterParams, Query(default=FilterParams())],
):
    return filter_query

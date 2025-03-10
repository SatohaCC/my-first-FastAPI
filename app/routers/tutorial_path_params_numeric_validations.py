from fastapi import APIRouter
from typing import Union
from typing import Annotated, Literal
from pydantic import BaseModel, Field
from fastapi import Path, Query

router = APIRouter()


# @router.get("/tutorial_path_params_numeric_validations/")
# async def read_item(
#     item_id: int = Path(title="The ID of the item to get"),
#     q: Union[str, None] = Query(default=None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


@router.get("/tutorial_path_params_numeric_validations/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@router.get("/tutorial_path_params_numeric_validations/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

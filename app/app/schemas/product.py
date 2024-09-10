from pydantic import BaseModel
from typing import List, Optional


class QuantityByWhSchema(BaseModel):
    """Схема для вложенной структуры данных quantity_by_wh."""
    wh: int
    quantity: int


class QuantityBySizesSchema(BaseModel):
    """Схема для вложенной структуры данных quantity_by_sizes."""
    size: str
    quantity_by_wh: List[QuantityByWhSchema]


class ProductSchema(BaseModel):
    """Схема для модели Product."""
    nm_id: int
    current_price: int
    sum_quantity: int
    image_url: Optional[str]
    quantity_by_sizes: List[QuantityBySizesSchema]

    class Config:
        orm_mode = True

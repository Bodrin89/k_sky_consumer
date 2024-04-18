from datetime import datetime

from pydantic import BaseModel


class ProductSchema(BaseModel):
    product_id: str
    quantity: int
    price: float
    category: str


class CheckSchema(BaseModel):
    transaction_id: str
    timestamp: datetime
    items: list[ProductSchema]
    total_amount: float
    nds_amount: float
    tips_amount: float
    payment_method: str
    place_name: str | None = None

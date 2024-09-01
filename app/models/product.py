from sqlalchemy import Column, Integer, JSON

from app.core.db import Base


class Product(Base):
    """Модель товара."""
    current_price = Column(Integer, nullable=False)
    sum_quantity = Column(Integer, nullable=False)
    quantity_by_sizes = Column(JSON, nullable=False)

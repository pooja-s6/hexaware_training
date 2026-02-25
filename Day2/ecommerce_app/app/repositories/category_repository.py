from sqlalchemy.orm import Session
from app.models.category import Category
from typing import List, Optional


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, category_data: dict) -> Category:
        category = Category(**category_data)
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def get_all_categories(self) -> List[Category]:
        return self.db.query(Category).all()

    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_category_by_name(self, name: str) -> Optional[Category]:
        return self.db.query(Category).filter(Category.name == name).first()
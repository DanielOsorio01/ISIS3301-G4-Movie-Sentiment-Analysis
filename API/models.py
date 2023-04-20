from sqlalchemy import String, Integer
from sqlalchemy.sql.schema import Column
from database import Base

class Review(Base):
    __tablename__ = "review_es"
    id = Column(Integer, primary_key=True, index=True)
    review_es = Column(String)
    classification = Column(String)
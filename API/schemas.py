from pydantic import BaseModel

"""
Este archivo contiene los modelos de datos que se utilizarán en la API.
"""
class CreateReview(BaseModel):
    review_es: str
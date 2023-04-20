from pydantic import BaseModel

class CreateReview(BaseModel):
    review_es: str
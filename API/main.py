from typing import List
import pandas as pd
import dataModel
from fastapi import FastAPI, Depends
from models import Review
from prediction_model import PredictionModel
from schemas import CreateReview
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, session

app = FastAPI()

origins = ["*"]

app.add_middleware(
      CORSMiddleware,
      allow_origins=origins,
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
)

Base.metadata.create_all(engine)
db = session

@app.on_event("startup")
async def startup_event():
   global prediction_model
   prediction_model = PredictionModel()

@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/predict")
def make_predictions(dataModel: list[dataModel.DataModel]):
   df = pd.DataFrame(x.dict() for x in dataModel)
   df.columns = dataModel[0].columns()
   results = prediction_model.make_prediction(df)
   return results.tolist()

@app.post("/postreview")
def create_review(review: CreateReview):
   gotclass = prediction_model.make_prediction(pd.DataFrame([review.review_es], columns=['review_es']))
   if gotclass[0] == 1:
      gotclass = 'Positivo'
   else:
      gotclass = 'Negativo'

   to_create = Review(review_es=review.review_es, classification=gotclass)
   db.add(to_create)
   db.commit()
   return {}

@app.get("/reviews", response_model=List[dataModel.Review])
def show_reviews():
   reviews = db.query(Review).all()
   return reviews

@app.get("/reviews/{review_id}", response_model=dataModel.Review)
def show_review(review_id: int):
   review = db.query(Review).filter(Review.id == review_id).first()
   return review
from typing import List
import pandas as pd
import dataModel
from fastapi import FastAPI
from models import Review
from prediction_model import make_prediction
from schemas import CreateReview
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, session
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, FileResponse


"""
Este es el archivo principal de la API, en este archivo se definen las rutas
y los métodos que se van a utilizar al momento de ejecutarse el API.
"""

# Se crea la instancia de FastAPI
app = FastAPI()
# Se definen los origenes permitidos para la API, en este caso se permite que cualquier origen se conecte a la API
origins = ["*"]

# Se agrega el middleware de CORS para permitir que cualquier origen se conecte a la API
app.add_middleware(
      CORSMiddleware,
      allow_origins=origins,
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
)

# Se crea la base de datos y se crea la sesión de la base de datos
Base.metadata.create_all(engine)
# Se crea la varibale para acceder a la base de datos
db = session

# La primera ruta es predefinida para mostrar un mensaje de bienvenida
@app.get("/")
def read_root():
   return FileResponse("index.html")

# Esta ruta permite realizar una prediccion de una entrada de texto
@app.post("/predict")
def make_predictions(dataModel: list[dataModel.DataModel]):
   df = pd.DataFrame(x.dict() for x in dataModel)
   df.columns = dataModel[0].columns()
   results = make_prediction(df)
   return results.tolist()

# Esta ruta permite crear una nueva review en la base de datos
@app.post("/postreview")
def create_review(review: CreateReview):
   # Se realiza la prediccion de la review recibida en la ruta
   gotclass = make_prediction(review.review_es)
   print (gotclass)
   # Se verifica si la prediccion es positiva o negativa
   if gotclass[0] == 1:
      gotclass = 'Positivo'
   else:
      gotclass = 'Negativo'
   # Se crea la review en la base de datos y se guarda
   reviewCreated = Review(review_es=review.review_es, classification=gotclass)
   db.add(reviewCreated)
   db.commit()
   response = {"id": reviewCreated.id, "body": reviewCreated.review_es, "sentiment": reviewCreated.classification}
   response = jsonable_encoder(response)
   return JSONResponse(content=response)

# Esta ruta permite mostrar todas las reviews de la base de datos
@app.get("/reviews", response_model=List[dataModel.Review])
def show_reviews():
   reviews = db.query(Review).all()
   return reviews

# Esta ruta permite mostrar una review en especifico de la base de datos
@app.get("/reviews/{review_id}", response_model=dataModel.Review)
def show_review(review_id: int):
   review = db.query(Review).filter(Review.id == review_id).first()
   return review

# Esta ruta permite eliminar una review en especifico de la base de datos
@app.delete("/delete")
def delete_reviews():
    db.query(Review).delete()
    db.commit()
    return {"message": "All reviews deleted"}
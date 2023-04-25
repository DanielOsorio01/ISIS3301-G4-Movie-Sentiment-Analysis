from pydantic import BaseModel

"""
Este archivo contiene los modelos de datos que se utilizarán en la API.
"""

class DataModel(BaseModel):
# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    review_es: str
#Esta función retorna los nombres de las columnas correspondientes con el modelo esxportado en pickle.
    def columns(self):
        return ['review_es']
    
# Esta clase permite que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
class Review(BaseModel):
    id: int
    review_es: str
    classification: str
    
    class Config:
        orm_mode = True

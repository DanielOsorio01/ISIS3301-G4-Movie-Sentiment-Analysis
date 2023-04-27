from sqlalchemy import String, Integer
from sqlalchemy.sql.schema import Column
from database import Base

"""
Se crea la clase Review que hereda de Base, la cual es la clase declarativa de SQLAlchemy.
Esta clase contiene las columnas de la tabla review_es de la base de datos.
"""
class Review(Base):
    # Se define el nombre de la tabla que se va a crear en la base de datos
    __tablename__ = "review_es"
    # Se define que el id es un entero y es la llave primaria de la tabla y se termina de definir las columnas
    id = Column(Integer, primary_key=True, index=True)
    review_es = Column(String)
    classification = Column(String)
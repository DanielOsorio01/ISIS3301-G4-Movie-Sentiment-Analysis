from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Se crea la conexion a la base de datos
engine = create_engine('sqlite:///aplicacion.sqlite')
# Se crea la sesion
Session = sessionmaker(bind=engine)

# Se crea la base de datos
Base = declarative_base()
# Se inicializa la sesion
session = Session()
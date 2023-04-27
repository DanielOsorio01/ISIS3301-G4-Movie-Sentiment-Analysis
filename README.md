# ISIS3301-G4-Movie-Sentiment-Analysis

## Integrantes
* Ángela Vargas - 201717106
* Juan Martin Santos - 202013610
* Daniel Osorio - 202022996

Para el despliegue de la API se deben seguir los siguientes pasos:
## 1. Instalacion de librerias 
Para ejecutar el API debemos encontrarnos en un ambiente con las librerias utilizadas, por lo que recomendamos usar Anaconda navigator que nos permite tener la mayoria de librerias.
Ademas instalaremos unas mas con los siguientes comandos:
* pip install fastapi
* pip install "uvicorn[standard]" 
* pip install langdetect
* pip install SQLAlchemy
* pip install pydantic

## 2. Ingresar a la carpeta para la ejecucion
Una vez tenemos las librerias necesarias para la ejeucion nos dirigimos a la carpeta del API desde la terminal con el siguiente comando:
* cd API

## 3. Ejecutar el back
Una vez estamos en la carpeta del API correremos el siguiente comando ejecutar el back:
* uvicorn main:app --reload
De esta forma el back ya estara desplegado para ser probado con las diferentes erramientas como postman o framworks para el front



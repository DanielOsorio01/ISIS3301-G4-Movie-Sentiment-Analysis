"""Codigo para crear el pipeline para el modelo de prediccion
y exportarlo para su uso en la API"""
import nltk
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from nltk.tokenize import wordpunct_tokenize
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from cleanText import cleanText
from langdetect import detect
nltk.download('stopwords')
import joblib as jb
import pandas as pd

# Funcion para eliminar los comentarios que no esten en es
def drop_lang(x):
    for index, row in x.iterrows():
        if detect(row['review_es']) != 'es':
            x.drop(index, inplace=True)
    return x

# Funcion para cambiar los valores de la columna sentimiento
def change_sentiment(x):
    x['sentimiento'].replace({'negativo' : 0, 'positivo' : 1}, inplace=True)
    return x

# Funcion para eliminar los duplicados y los nulos
def dropper(x):
    x = x.drop(["Unnamed: 0"], axis=1) # Assign the modified DataFrame to x
    x['review_es'].drop_duplicates(inplace=True)
    x['review_es'].dropna(inplace=True)
    return x

preprocessing = Pipeline([
    ('drop_lang', FunctionTransformer(drop_lang)),
    ('dropper', FunctionTransformer(dropper)),
    ('change_sentiment', FunctionTransformer(change_sentiment)),
])

vectorizer = jb.load('./data/count_vectorizer.pkl')
pipeline = Pipeline([
    ('clean_text', cleanText()),
    ('Vectorizer', vectorizer),
    ('Model', LogisticRegression(max_iter=1000,solver='newton-cg'))
])

# Cargamos los datos para realizar el entrenamiento del modelo
df = pd.read_csv('API/data/MovieReviews.csv')

# Limpiamos los datos
df = preprocessing.fit_transform(df)

x = df['review_es']
y = df['sentimiento']

# Hacemos el split de los datos para entrenar el modelo
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Entrenamos el modelo
pipeline.fit(X_train, y_train)

# Guardamos y exportamos el modelo
jb.dump(pipeline, 'API/data/prediccion_reviews.pkl')

# Probamos el modelo
print(pipeline.score(X_test, y_test))

# Realizamos una prediccion muy basica y la imprimimos para ver el resultado, si es 0 es negativo de lo contrario positivo
text = ['Odie la película, es muy mala']
df_test = pd.DataFrame({'review_es': text})
prediction = pipeline.predict(df_test['review_es'])
print(prediction)
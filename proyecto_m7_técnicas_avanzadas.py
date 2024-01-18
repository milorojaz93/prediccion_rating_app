# -*- coding: utf-8 -*-
"""Proyecto M7. Técnicas avanzadas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lh1PKhfdE6Zq-AAkeG7Yrxn7IJ_qmSpX

## **Bootcamp: Ciencia de Datos e Inteligencia Artificial**
## **Proyecto del Módulo 7: Técnicas avanzadas para ciencia de datos y empleabilidad**

Hola, ya es el último proyecto, has avanzado y aprendido mucho hasta acá. ¡Muchas felicidades!

Es hora de poner en práctica todo lo que hemos aprendido a lo largo de nuestra travesía.

Lee el proyecto y revisa con cuidado cada una de las instrucciones. Procura plasmar todo tu potencial para que lo concluyas de manera sobresaliente.

¡Éxito!
"""

import sys

print("Versión de Python:")
print(sys.version)
print("Versión de Python info:")
print(sys.version_info)

"""# Objetivos
- Aplicar con éxito todos los conocimientos que has adquirido a lo largo del Bootcamp.
- Consolidar las técnicas de limpieza, entrenamiento, graficación y ajuste a modelos de *Machine Learning*.
- Generar una API que brinde predicciones como resultado a partir de datos enviados.

# Proyecto

1. Selecciona uno de los siguientes *datasets*:
  - *Reviews* de aplicaciones de la Google Play Store: https://www.kaggle.com/datasets/lava18/google-play-store-apps
  - Estadísticas demográficas de los ganadores del premio Oscar de la Academia: https://www.kaggle.com/datasets/fmejia21/demographics-of-academy-awards-oscars-winners
  - Aspiraciones profesionales de la generación Z: https://www.kaggle.com/datasets/kulturehire/understanding-career-aspirations-of-genz

Cada uno representa un *dataset*, un problema y una forma diferente de abordarlo. Tu tarea es identificar las técnicas y modelos que podrías usar para tu proyecto.

2. Debes hacer un análisis exploratorio y limpieza de los datos. Usa las ténicas que creas convenientes.

3. Entrena el modelo de *Machine Learning*, procesamiento de lenguaje natural o red neuronal que creas adecuado.

4. Genera por lo menos dos gráficas y dos métricas de rendimiento; explica las puntuaciones de rendimiento que amerite tu problema. Todas las gráficas de rendimiento que realices deben tener leyendas, colores y títulos personalizados por ti.

  - Además, antes de subir el modelo a "producción", deberás realizar un proceso de ensambles (*ensemblings*) y de ajuste de hiperparámetros o *tuning* para intentar mejorar la precisión y disminuir la varianza de tu modelo.

5. Construye una API REST en la que cualquier usuario pueda mandar datos y que esta misma devuelva la predicción del modelo que has hecho. La API debe estar en la nube, ya sea en un servicio como Netlify o Ngrok, para que pueda ser consultada desde internet.

6. Genera una presentación del problema y del modelo de solución que planteas. Muestra gráficas, datos de rendimiento y explicaciones. Esta presentación debe estar enfocada a personas que no sepan mucho de ciencia de datos e inteligencia artificial.

7. **Solamente se recibirán trabajos subidos a tu cuenta de GitHub con un README.md apropiado que explique tu proyecto**.

## Criterios de evaluación

| Actividad | Porcentaje | Observaciones | Punto parcial
| -- | -- | -- | -- |
| Actividad 1. Limpieza y EDA | 20 | Realiza todas las tareas necesarias para hacer el EDA y la limpieza correcta, dependiendo de la problemática. Debes hacer como mínimo el análisis de completitud, escalamiento (si aplica) y tokenización (si aplica). | Realizaste solo algunas tareas de exploración y limpieza y el modelo se muestra aún con oportunidad de completitud, escalamiento y/o mejora. |
| Actividad 2. Entrenamiento del modelo | 20 | Elige el modelo y algoritmo adecuados para tu problema, entrénalo con los datos ya limpios y genera algunas predicciones de prueba. | No has realizado predicciones de prueba para tu modelo de ML y/o tu modelo muestra una precisión menor al 60 %. |
| Actividad 3. Graficación y métricas | 20 | Genera por lo menos dos gráficas y dos muestras de métricas que permitan visualizar el rendimiento y precisión del modelo que construiste. Además, realizaste los procesos de *tuning* y ensambles adecuados para tu problema. | Las gráficas no tienen leyendas y colores customizados, solo muestras una gráfica o no realizaste el *tuning* de hiperparámetros.
| Actividad 4. API REST | 20 | Generaste con éxito un *link* público en el que, por método POST, se puede mandar información y la API REST devuelve una predicción junto con el porcentaje de confianza de esta misma. | N/A
| Actividad 5. Presentación | 20 | Genera una presentación en la que establezcas como mínimo: el problema, proceso de solución, metodologías usadas, gráficas de rendimiento, demostración del modelo y aprendizajes obtenidos. Debes redactarla con términos que pueda entender cualquier persona, no solo científicos de datos. | La presentación no expone con claridad o en términos coloquiales el proceso de creación del modelo, sus ventajas y muestras de rendimiento.

**Mucho éxito en tu camino como Data Scientist.**
"""

# Importamos librerias correspondients
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #No quitar
import seaborn as sns
from google.colab import drive
drive.mount('/content/drive')
from sklearn.preprocessing import LabelEncoder

ds_apps  = pd.read_csv('/content/drive/MyDrive/BOTTCAMPS/PJ7- apps.csv', encoding='ISO-8859-1')
ds_reviews = pd.read_csv('/content/drive/MyDrive/BOTTCAMPS/PJ7 -apps_reviwes.csv')

ds_apps.head()

ds_apps.info()

# Iniciamos validando la data categorica
print(ds_apps['Category'].unique())
# Usamos labelencoder para decodificar estas categorias
label_encoder = LabelEncoder()
ds_apps['n_Category'] = label_encoder.fit_transform(ds_apps['Category'])
print(ds_apps['n_Category'].unique())

fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(ds_apps['Category'].value_counts().index, ds_apps['Category'].value_counts().values)
ax.set_title('Categorías de apps')
ax.set_xlabel('Cantidad')
ax.set_ylabel('Categoría')
plt.show()

# Continuamos ahora con la columna rating
print(ds_apps['Rating'].unique())
#Actualizamos una columna para identifica si se calificó o no la app, 0 no 1 si
ds_apps['Calified'] = (ds_apps['Rating'].isnull() == False).astype(int)

ds_apps.head()

# Imputar los NaN con la mediana de las calificaciones
mediana = ds_apps['Rating'].median()
ds_apps['Rating'] = ds_apps['Rating'].fillna(mediana)
ds_apps['Rating'] = ds_apps['Rating'].apply(lambda x : mediana if x > 5 else x)
print(ds_apps['Rating'].unique())

sns.histplot(data=ds_apps, x='Rating',kde=True)
plt.axvline(ds_apps['Rating'].mean(), color='r', label='Media')
plt.axvline(ds_apps['Rating'].max(), color='g', ls='--', label='Valor Max')
plt.axvline(ds_apps['Rating'].min(), color='g', ls='--', label='Valor Min')
plt.xlabel('Rating')
plt.ylabel('Cantidad')
plt.legend()

plt.figure(figsize=(18,7))
sns.boxplot(data=ds_apps, x='Rating')
plt.xticks(rotation = 45)
plt.title('BoxPlot Rating')
plt.tight_layout()

#Ahora validamos la columna size y la pasamos a datos numericos en M
print(ds_apps['Size'].unique())
# Convertir los tamaños a MB
def convertir_a_mb(size):
    if pd.isna(size):
        return pd.NA
    elif 'k' in size:
        return float(size.replace('k', '')) / 1024
    elif 'M' in size:
        return float(size.replace('M', ''))
    else:
        return pd.NA

ds_apps['Size_MB'] = ds_apps['Size'].apply(convertir_a_mb)
mediana = ds_apps['Size_MB'].median()
ds_apps['Size_MB'] = ds_apps['Size_MB'].fillna(mediana)
print(ds_apps['Size_MB'].unique())

plt.scatter(x=ds_apps['Size_MB'], y=ds_apps['Rating'])
plt.xlabel('Tamaño en MB')
plt.ylabel('Rating')
plt.title('Tamaño vs Rating')
plt.show()

#Ahora validamos la columna size y la pasamos a datos numericos en M
print(ds_apps['Installs'].unique())
# Mapear 'Free' a 0
ds_apps['Installs'] = ds_apps['Installs'].replace('Free', '0')

# Eliminar símbolos no deseados y convertir a tipo numérico
ds_apps['Installs_clean'] = ds_apps['Installs'].str.replace('[+,]', '', regex=True).astype(int)

# Imprimir el DataFrame resultante
print(ds_apps['Installs_clean'].unique())

sns.histplot(data=ds_apps, x='Installs_clean',kde=True)
plt.axvline(ds_apps['Installs_clean'].mean(), color='r', label='Media')
plt.axvline(ds_apps['Installs_clean'].max(), color='g', ls='--', label='Valor Max')
plt.axvline(ds_apps['Installs_clean'].min(), color='g', ls='--', label='Valor Min')
plt.xlabel('Installs_clean')
plt.ylabel('Cantidad')
plt.legend()

plt.figure(figsize=(18,7))
sns.boxplot(data=ds_apps, x='Installs_clean')
plt.xticks(rotation = 45)
plt.title('BoxPlot Rating')
plt.tight_layout()

#Ahora el tipo de app la ponemos en 0 como gratis, 1 como pago y 2 como sin clasificar
print(ds_apps['Type'].unique())
# Mapear las etiquetas a valores numéricos
mapping = {'Free': 0, 'Paid': 1, '0': 2}
ds_apps['Decoded_Type'] = ds_apps['Type'].map(mapping)
ds_apps['Decoded_Type'] = ds_apps['Decoded_Type'].fillna(2)
print(ds_apps['Decoded_Type'].unique())

fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(ds_apps['Type'].value_counts().index, ds_apps['Type'].value_counts().values)
ax.set_title('Tipo de apps')
ax.set_xlabel('Cantidad')
ax.set_ylabel('Tipo')
plt.show()

print(ds_apps['Price'].unique())
ds_apps['Price_clean'] = pd.to_numeric(ds_apps['Price'].replace('[\$,]', '', regex=True), errors='coerce')

# Imprimir el DataFrame resultante
print(ds_apps['Price_clean'].unique())

df_nulos = ds_apps.loc[ds_apps['Price_clean'].isnull()].count()

# Imprimimos para saber cuantas filas tienen el dato nulo
print(df_nulos)
ds_apps['Price_clean'] = ds_apps['Price_clean'].fillna(0)

plt.scatter(x=ds_apps['Price_clean'], y=ds_apps['Rating'])
plt.xlabel('Precio')
plt.ylabel('Rating')
plt.title('Precio vs Rating')
plt.show()

print(ds_apps['Content Rating'].unique())
# Crear una instancia de LabelEncoder
label_encoder = LabelEncoder()

# Rellenar los valores nulos con una categoría adicional, por ejemplo, 'Unknown'
ds_apps['Content Rating'].fillna('Unknown', inplace=True)

# Aplicar el LabelEncoder a la columna 'Content Rating'
ds_apps['Content_Rating_Enc'] = label_encoder.fit_transform(ds_apps['Content Rating'])

# Imprimir el DataFrame resultante
print(ds_apps['Content_Rating_Enc'].unique())



fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(ds_apps['Content Rating'].value_counts().index, ds_apps['Content Rating'].value_counts().values)
ax.set_title('Categoria de apps')
ax.set_xlabel('Cantidad')
ax.set_ylabel('Categoría')
plt.show()

print(ds_apps['Genres'].unique())
ds_genres = ds_apps['Genres'].str.get_dummies(sep=';')
ds_genres

ds_apps = ds_apps.join(ds_genres)
ds_apps

from datetime import datetime

# Convertir la columna 'Last Updated' al formato de fecha
ds_apps['Last Updated'] = pd.to_datetime(ds_apps['Last Updated'], format='%B %d, %Y', errors='coerce')

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular los días transcurridos
ds_apps['DaysUpdate'] = (fecha_actual - ds_apps['Last Updated']).dt.days

# Mostrar el DataFrame resultante
print(ds_apps['DaysUpdate'])

sns.histplot(data=ds_apps, x='DaysUpdate',kde=True)
plt.axvline(ds_apps['DaysUpdate'].mean(), color='r', label='Media')
plt.axvline(ds_apps['DaysUpdate'].max(), color='g', ls='--', label='Valor Max')
plt.axvline(ds_apps['DaysUpdate'].min(), color='g', ls='--', label='Valor Min')
plt.xlabel('DaysUpdate')
plt.ylabel('Cantidad')
plt.legend()

plt.scatter(x=ds_apps['DaysUpdate'], y=ds_apps['Rating'])
plt.xlabel('DaysUpdate')
plt.ylabel('Rating')
plt.title('DaysUpdate vs Rating')
plt.show()

ds_reviews

# Crear una máscara booleana para valores nulos en la columna 'Size_MB'
valores_nulos = ds_reviews['Translated_Review'].isnull()

# Filtrar el DataFrame para mostrar solo los registros con valores nulos
registros_nulos = ds_reviews[valores_nulos]

# Mostrar los registros nulos
print(registros_nulos.count())

ds_reviews = ds_reviews.loc[~valores_nulos]
ds_reviews

import string
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# Vamos a remover las urls
def quitar_urls(texto):
    # Patrón de expresión regular para encontrar URLs
    patron_url = re.compile(r'https?://\S+|www\.\S+')

    # Reemplazar las URLs con una cadena vacía
    texto_sin_urls = patron_url.sub('', texto)

    return texto_sin_urls

PUNCT_TO_REMOVE = string.punctuation
def remover_pun(texto):
  return texto.translate(str.maketrans('','',PUNCT_TO_REMOVE))

ds_reviews['Translated_Review_clean'] = ds_reviews['Translated_Review'].apply(lambda texto: quitar_urls(texto))
ds_reviews['Translated_Review_clean'] = ds_reviews['Translated_Review_clean'].apply(lambda texto: remover_pun(texto))
# removemos espacios, numeros y stopwords
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def remove_stopwords(texto):
  texto = ''.join(caracter for caracter in texto if caracter.isalpha() or caracter.isspace())
  return " ".join([palabra for palabra in str(texto).split() if palabra not in ENGLISH_STOP_WORDS])

ds_reviews['Translated_Review_clean'] = ds_reviews['Translated_Review_clean'].apply(lambda texto: remove_stopwords(texto))
ds_reviews.head()

# prompt: Generar grafica de barrar de Sentiment

fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(ds_reviews['Sentiment'].value_counts().index, ds_reviews['Sentiment'].value_counts().values)
ax.set_title('Sentimiento de las reseñas')
ax.set_xlabel('Cantidad')
ax.set_ylabel('Sentimiento')
plt.show()

# prompt: create a dataframe with 2 columns and 10 rowsuiero grafica scatter Sentiment_Polarity vs Sentiment_Subjectivity

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #No quitar
import seaborn as sns

df = pd.DataFrame({'Sentiment_Polarity': np.random.randn(10), 'Sentiment_Subjectivity': np.random.randn(10)})
plt.scatter(x=df['Sentiment_Polarity'], y=df['Sentiment_Subjectivity'])
plt.xlabel('Sentiment_Polarity')
plt.ylabel('Sentiment_Subjectivity')
plt.title('Sentiment_Polarity vs Sentiment_Subjectivity')
plt.show()

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

# Supongamos que ya tienes un DataFrame llamado ds_reviews
# y que tienes una columna llamada 'Sentiment' y otra llamada 'Translated_Review_clean'

# Crear una figura con 2x2 subgráficos
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('WordClouds por Sentimiento', fontsize=16)

# Iterar sobre los sentimientos y crear WordCloud para cada uno
sentimientos = ds_reviews['Sentiment'].unique()
for i, sentimiento in enumerate(sentimientos):
    # Filtrar texto por sentimiento
    texto = " ".join(texto for texto in ds_reviews[ds_reviews['Sentiment'] == sentimiento]['Translated_Review_clean'])

    # Crear WordCloud
    wd = WordCloud().generate(texto)

    # Mostrar WordCloud en el subgráfico correspondiente
    axs[i//2, i%2].imshow(wd, interpolation='bilinear')
    axs[i//2, i%2].set_title(sentimiento)
    axs[i//2, i%2].axis('off')

# Ajustar el diseño de la figura y mostrarla
plt.tight_layout(rect=[0, 0, 1, 0.96])  # rect ajusta el espacio superior para el título
plt.show()

#Ahora el tipo de app la ponemos en 0 como gratis, 1 como pago y 2 como sin clasificar
print(ds_reviews['Sentiment'].unique())
# Mapear las etiquetas a valores numéricos
mapping = {'Positive': 1, 'Neutral': 0, 'Negative': -1}
ds_reviews['Sentiment_Label'] = ds_reviews['Sentiment'].map(mapping)
print(ds_reviews['Sentiment_Label'].unique())

X = ds_reviews['Translated_Review_clean']
Y = ds_reviews['Sentiment_Label']
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(token_pattern='\\b\\w+\\b')
train_matrix = cv.fit_transform(x_train)
test_matrix = cv.transform(x_test)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(train_matrix, y_train)
y_pred = knn.predict(test_matrix)
from sklearn.metrics import  classification_report,ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_predictions(y_test, y_pred)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)
# Entrenar el modelo
random_forest_model.fit(train_matrix, y_train)

# Realizar predicciones en el conjunto de prueba
predicciones = random_forest_model.predict(test_matrix)

# Evaluar la precisión del modelo
accuracy = accuracy_score(y_test, predicciones)
print(f"Precisión del modelo: {accuracy}")

# Imprimir el informe de clasificación
print("Informe de clasificación:\n", classification_report(y_test, predicciones))

import joblib
joblib.dump(knn, 'knn2.pkl')

import joblib
joblib.dump(cv, 'mensajes_cv.pkl')



# Utilizar pivot_table para expandir la columna 'sentimiento' en tres nuevas columnas
ds_reviews_Pivot = ds_reviews[['App','Sentiment_Label']].pivot_table(index='App', columns='Sentiment_Label', aggfunc='size').reset_index()

# Renombrar las columnas
ds_reviews_Pivot.columns.name = None  # Eliminar el nombre de la columna de los sentimientos
ds_reviews_Pivot = ds_reviews_Pivot.rename(columns={ -1: 'Count_Negative', 0: 'Count_Neutral', 1: 'Count_Positive'})

# Mostrar el DataFrame resultante
ds_reviews_Pivot

# Sumar los valores de las columnas 'sentimiento_positivo', 'sentimiento_negativo', y 'sentimiento_neutral'
ds_reviews_Pivot['total_sentimientos'] = ds_reviews_Pivot[['Count_Negative', 'Count_Neutral', 'Count_Positive']].sum(axis=1)

# Convertir a porcentajes
columnas_sentimientos = ['Count_Negative', 'Count_Neutral', 'Count_Positive']
for columna in columnas_sentimientos:
    ds_reviews_Pivot[columna] = (ds_reviews_Pivot[columna] / ds_reviews_Pivot['total_sentimientos']) * 100

# Eliminar la columna de totales si ya no es necesaria
ds_reviews_Pivot = ds_reviews_Pivot.drop(columns=['total_sentimientos'])
ds_reviews_Pivot

df_resultado = pd.merge(ds_apps, ds_reviews_Pivot, on='App', how='inner')
df_resultado.count()

df_resultado = df_resultado.drop(columns=['App','Category','Price', 'Size', 'Installs', 'Type','Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver'])
df_resultado

json_output = df_resultado.iloc[0].to_json()
json_output

# Imputar los NaN con la mediana de las Negativos
mediana = df_resultado['Count_Negative'].median()
df_resultado['Count_Negative'] = df_resultado['Count_Negative'].fillna(mediana)

# Imputar los NaN con la mediana de las neutrales
mediana = df_resultado['Count_Neutral'].median()
df_resultado['Count_Neutral'] = df_resultado['Count_Neutral'].fillna(mediana)

# Imputar los NaN con la mediana de las Positivos
mediana = df_resultado['Count_Positive'].median()
df_resultado['Count_Positive'] = df_resultado['Count_Positive'].fillna(mediana)

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

x = df_resultado.drop(["Rating"], axis=1)
y = df_resultado.Rating

scaler = StandardScaler().fit(x)
x_standar = scaler.transform(x)

pca = PCA(n_components = 2)
x_new = pca.fit_transform(x_standar)
x_new.shape

import joblib
joblib.dump(pca, 'pca.pkl')

plt.style.use('ggplot')

exp_var = pca.explained_variance_ratio_ * 100
cum_exp_var = np.cumsum(exp_var)
plt.bar(range(1, 3), exp_var, align='center', color= 'blue',
        label='Varianza Individual')

plt.step(range(1, 3), cum_exp_var, where='mid',
         label='Varianza Acumulativa', color='red')

plt.ylabel('Porcentaje de varianza')
plt.xlabel('Componentes')
plt.xticks(ticks=[1, 2])
plt.legend(loc='best')
plt.tight_layout()

plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Dividir el conjunto de datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = modelo.predict(X_test)

# Calcular métricas de rendimiento
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Mostrar métricas de rendimiento
print(f'Mean Squared Error (MSE): {mse}')
print(f'R-squared (R2): {r2}')

import joblib
joblib.dump(modelo, 'lr.pkl')


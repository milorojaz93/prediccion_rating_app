import string
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import warnings
# from sklearn.exceptions import InconsistentVersionWarning
# Vamos a remover las urls
def quitar_urls(texto):
    # Patrón de expresión regular para encontrar URLs
    patron_url = re.compile(r'https?://\S+|www\.\S+')

    # Reemplazar las URLs con una cadena vacía
    texto_sin_urls = patron_url.sub('', texto)

    return texto_sin_urls

def remover_pun(texto):
    PUNCT_TO_REMOVE = string.punctuation
    return texto.translate(str.maketrans('','',PUNCT_TO_REMOVE))

# removemos espacios, numeros y stopwords
def remove_stopwords(texto):
  texto = ''.join(caracter for caracter in texto if caracter.isalpha() or caracter.isspace())
  return " ".join([palabra for palabra in str(texto).split() if palabra not in ENGLISH_STOP_WORDS])

def limpiar_mensajes(ds_reviews):
    #warnings.simplefilter("ignore", InconsistentVersionWarning)
    ds_reviews[0] = ds_reviews[0].apply(lambda texto: remove_stopwords(texto))
    ds_reviews[0] = ds_reviews[0].apply(lambda texto: quitar_urls(texto))
    ds_reviews[0] = ds_reviews[0].apply(lambda texto: remover_pun(texto))
    cv = joblib.load('mensajes_cv.pkl')
    datos = cv.transform(ds_reviews[0])
    return datos


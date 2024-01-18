from flask import Flask, request, jsonify
import pandas as pd
import joblib
from cleaning import limpiar_mensajes
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import json

app = Flask(__name__)

@app.route('/predecir', methods=['POST'])
def predict():
    try:
        json_ = request.json
        mensajes  = json_['aMensajes']  # Obtener el valor asociado con 'mensajes'
        del json_['aMensajes']  # Eliminar la clave 'mensajes' del objeto JSON
        ds_mensajes = pd.DataFrame(mensajes)

        knn = joblib.load('knn.pkl')
        ds_mensajes = limpiar_mensajes(ds_mensajes)
        prediction = knn.predict(ds_mensajes)
        dataframe = pd.DataFrame(prediction)
        # Sacamos nuevas columnas
        n_negativos = dataframe[(dataframe[0] == -1)].count()
        n_neutros = dataframe[(dataframe[0] == 0)].count()
        n_positivos = dataframe[(dataframe[0] == 1)].count()

        total = n_negativos + n_neutros + n_positivos

        n_negativos = n_negativos / total
        n_positivos = n_positivos / total
        n_neutros = n_neutros / total
        json_['Count_Negative'] = n_negativos
        json_['Count_Neutral'] = n_neutros
        json_['Count_Positive'] = n_positivos
        query_df = pd.DataFrame(json_)

        #scaler = StandardScaler().fit(query_df)
        #x_standar = scaler.transform(query_df)

        #pca = joblib.load('pca.pkl')
        #x_new = pca.fit_transform(x_standar)

        lr = joblib.load('lr.pkl')
        prediction = lr.predict(query_df)

        # Convert the NumPy array to a list
        list_of_lists = prediction.tolist()

        # Convert the list of lists to JSON
        json_data = json.dumps(list_of_lists)
        return json_data

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

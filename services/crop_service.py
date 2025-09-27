import pickle

import numpy as np
from schemas.crop_schemas import CropData


# Cargamos el modelo de RandomForest

with open('RFCrop.pkl', 'rb') as file:
    rf_model = pickle.load(file)

with open('SVMCrop.pkl', 'rb') as file:
    svm_model = pickle.load(file)


labels=['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
def crop_prediction(data: CropData, model_choice="rf"):
    # Aquí iría la lógica para hacer la predicción usando el modelo entrenado
    xin=np.array([[data.N, 
                   data.P, 
                   data.K,
                   data.temperature,
                   data.humidity, 
                   data.ph,
                   data.rainfall,
                   ]]).reshape(1, 7)


    if data.model_choice == "rf":
                         prediction = rf_model.predict(xin)
                         model_name = "RandomForest"
    else:
                          prediction = svm_model.predict(xin)
                          model_name = "SVM"
    print(f"Modelo usado: {model_name}")
    print(f"Predicción: {prediction[0]}")
    return prediction[0]
   
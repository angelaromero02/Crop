import pickle

import numpy as np
from schemas.crop_schemas import CropData


# Cargamos el modelo de RandomForest

with open('RFCrop.pkl','rb') as file:
    model = pickle.load(file)
labels=['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
def crop_prediction(data: CropData):
    # Aquí iría la lógica para hacer la predicción usando el modelo entrenado
    xin=np.array([[data.N, 
                   data.P, 
                   data.K,
                   data.temperature,
                   data.humidity, 
                   data.ph,
                   data.rainfall,
                   ]]).reshape(1, 7)


    prediction = model.predict(xin)

    print("predicción:",prediction)
    # Por simplicidad, vamos a devolver una predicción ficticia
    return prediction[0]
   
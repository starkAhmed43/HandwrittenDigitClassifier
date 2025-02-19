import pickle
import uvicorn
from utils import *
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from dense_neural_class import *

class ImageVector(BaseModel):
    image_json: dict

def load_model(path):   
    with open(path, 'rb') as file:
        return pickle.load(file)
    
model = load_model(Path('./model.pkl'))
    
def predict(image_vector):
    result = model.predict(image_vector)
    return int(result)

inference_app = FastAPI()

@inference_app.post('/predict')
def get_prediction(image_vector: ImageVector):
    image_json = image_vector.image_json
    image_vector = [image_json[f'pixel_{i}'] for i in range(28 * 28)]
    image_vector = np.array(image_vector).reshape(-1,)
    return {'prediction': predict(image_vector)}

if __name__ == '__main__':
    uvicorn.run(inference_app, host='localhost', port=5402)
from pydantic import BaseModel

class CropData(BaseModel):
    N: int
    P: int
    K: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float
    model_choice: str = "rf"
    


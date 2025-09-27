from fastapi import APIRouter

from schemas.crop_schemas import CropData
from services.crop_service import crop_prediction


router = APIRouter()


@router.post("/predict")
async def crop_predict(data: CropData):
    print(f"Crop data: N={data.N}, P={data.P}, K={data.K}, temperature={data.temperature}, humidity={data.humidity}, ph={data.ph}, rainfall={data.rainfall}")
    
    prediction = crop_prediction(data)

    return {"prediction": prediction}
from fastapi import APIRouter,Path
from schemas.health import BMIResult, health

router = APIRouter()

@router.get("/healthcheck/{name}/{weight}/{height}", response_model=BMIResult)
async def health_check(name: str, weight: float, height: float):
    w=(height/100)**2
    bmi = weight/w
    return BMIResult(name=name, weight=weight, height=height, bmi=bmi)


from fastapi import APIrouter,Path
from schemas.health import health

router = APIRouter()

@router.get("/BMI/")
def BMI_check(H:health= Path(...,le=0),W:health =Path(...,le=0) 
):
   H= H/100
   bmi=W//H*H
   return {"msg":f'{bmi}'}
 

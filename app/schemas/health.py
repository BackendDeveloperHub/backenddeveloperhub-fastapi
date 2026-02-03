
from pydantic import BaseModel



class health(BaseModel):
   name:str
   weight:float
   height:float

class BMIResult(BaseModel):
   name:str
   weight:float
   height:float
   bmi:float
   


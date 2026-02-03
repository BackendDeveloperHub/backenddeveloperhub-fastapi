
from pydantic import BaseModel



class health(BaseModel):
   name:str
   weight:float
   height:float

class User(BaseModel):
   pass



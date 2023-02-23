from pydantic import BaseModel,Field
from typing import List,Optional
#要run程式的話直接在terminal輸入  python.exe .\main.py
# database


class DrugIn(BaseModel):
    medname:str
    eat_time:list[str] |None
    no:int
    descrp:str |None=None
    weekly:list[str]
    
    
class Drug(DrugIn):
    id:int
    class Config:
        orm_mode=True

from pydantic import BaseModel,Field
from typing import List,Optional
#要run程式的話直接在terminal輸入  python.exe .\main.py
# database


class EventIn(BaseModel):
    event_type :str
    message :str
    data :dict | None
    class Config:
        orm_mode=True 
    
class Event(EventIn):
    id:int
    class Config:
        orm_mode=True
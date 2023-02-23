from fastapi import FastAPI,Depends
from fastapi import FastAPI
from pydantic import BaseModel
#要run程式的話直接在terminal輸入  python.exe .\main.py
# database
from sqlalchemy.orm import Session
from database.database import get_db
from database.database import create_table
#1.這裡將資料庫匯入後
import database.models.events
import database.models.drugs
import database.models.User

app = FastAPI()
items=[]
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://192.168.0.131:8080",
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    medname:str
    eat_time:list[str] |None
    no:int
    descrp:str |None=None
    weekly:list[str]
    
@app.on_event ('startup')
def startup():
  pass




    
@app.post("/items/")
async def create_item(item:Item):
    items.append(item)
    return {"status":"success"}

@app.get("/items/",response_model=list[Item])
async def get_item():
    return items

#2.到這裡使用get post (記得同時額外建event.py)
import base_models.event 
@app.get('/events',response_model=list[base_models.event.Event])
async def getMsgs(db :Session = Depends(get_db)):
    return database.models.events.Event.get_messages(db)

@app.post('/events',response_model=base_models.event.EventIn)
async def CreateMsg(msgIn : base_models.event.EventIn ,db :Session = Depends(get_db) ):
    newEvent=database.models.events.Event()
    newEvent.event_type = msgIn.event_type
    newEvent.message = msgIn.message
    newEvent.dt = msgIn.data
    newEvent.save_to_db(db)
    return msgIn


import base_models.drug 
@app.get('/drugs',response_model=list[base_models.drug.Drug])
async def getMsgs(db :Session = Depends(get_db)):
    return database.models.drugs.Drug.get_messages(db)

@app.post('/drugs',response_model=dict)
async def CreateMsg(msgIn : base_models.drug.DrugIn ,db :Session = Depends(get_db) ):
    newDrug=database.models.drugs.Drug()
    newDrug.medname = msgIn.medname
    newDrug.eat_time = msgIn.eat_time
    newDrug.no = msgIn.no
    newDrug.descrp = msgIn.descrp
    newDrug.weekly = msgIn.weekly
    newDrug.save_to_db(db)
    return msgIn


@app.post('/createUser',response_model=dict)
async def CreateUser(db :Session = Depends(get_db) ):
    newUser = database.models.User.User()
    newUser.user_name = "persephone"
    newUser.save_to_db(db)
    return {}

@app.get('/getuser/{username}')
async def getuser(username:str ,db :Session = Depends(get_db) ):
    return database.models.User.User.get_uesr_by_username(db,username=username)

if __name__== "__main__":
    import uvicorn
    create_table()
    uvicorn.run("main:app", host ="0.0.0.0", port=81 , reload=True)

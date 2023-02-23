from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,JSON
from sqlalchemy.orm import relationship, Session
from ..database import Base

class Event(Base):
    # 資料表名稱(下面)
    __tablename__ = "event"
    id = Column(Integer, primary_key=True,index=True,unique=True) #如果要是唯一的就上unique(primary key不要刪<每一個都要)
    event_type = Column(String(150))
    message = Column(String(150))
    data = Column(JSON)
    user_id = Column(Integer,ForeignKey("user.id"))

    @staticmethod
    def get_message_by_id(db: Session, id: int):#db變數是session(對話)的型態
        return db.query(Event).filter(Event.id == id).first()
    @staticmethod
    def get_messages(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Event).offset(skip).limit(limit).all()

    def save_to_db(self, db: Session):
        db.add(self)
        db.commit()
        db.refresh(self)

       
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship, Session
# from ..database import Base

# class Message(Base):
#     # 資料表名稱(下面)
#     __tablename__ = "messages"
#     id = Column(Integer, primary_key=True,index=True,unique=True) #如果要是唯一的就上unique
#     nick_name = Column(String(150))
#     message = Column(String(50),index=True)
    
#     @staticmethod
#     def get_message_by_id(db: Session, id: int):#db變數是session(對話)的型態
#         return db.query(Message).filter(Message.id == id).first()
#     @staticmethod
#     def get_messages(db: Session, skip: int = 0, limit: int = 100):
#         return db.query(Message).offset(skip).limit(limit).all()

#     def save_to_db(self, db: Session):
#         db.add(self)
#         db.commit()
#         db.refresh(self)
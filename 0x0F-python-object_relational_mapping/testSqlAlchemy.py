#!/usr/bin/env python3

#connecting
from sqlalchemy import create_engine
# Declare a Mapping
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker


#Create a session 
Session = sessionmaker() # If no Engine avalaible ()
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(100))
    nickname = Column(String(50))

    def __repr__(self):
        return (f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname}>")

#print(User.__table__)

#Create a SCHEMA
Base.metadata.create_all(engine)


ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
#print(ed_user.name)

Session.configure(bind=engine) #once engine is available
session = Session()
session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
#print(our_user)

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

ed_user.nickname = 'eddie'

## modified session
#print(session.dirty)

## Show pending
#print(session.new)

# Flush the remaining the changes to the database
session.commit()

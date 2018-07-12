from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from ENV import app

db = SQLAlchemy(app)

class Rooms(db.Model):
  __tablename__ = 'Rooms'
  ID = db.Column(db.Integer, primary_key=True)
  RoomName = db.Column(db.String(16), nullable=False)

  def json(self):
    return {'RoomName': self.RoomName, 'ID': self.ID}
  
  def create_room(_roomName):
    new_room = Rooms(RoomName=_roomName)
    db.session.add(new_room)
    db.session.commit()

  def get_all_rooms():
    all_rooms = []
    for e in Rooms.query.all():
      all_rooms.append(Rooms.json(e))
    return all_rooms

  def get_room_by_string(_query):
    return Rooms.query.filter_by(RoomName=_query).first()

  def get_room_by_id(_ID):
    return Rooms.query.filter_by(ID=_ID).first()

  def __repr__(self):
    user_object = {
      'roomName': self.RoomName,
      'ID': self.ID,
      }
    return json.dumps(user_object)
 
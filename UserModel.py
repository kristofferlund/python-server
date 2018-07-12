from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from ENV import app

db = SQLAlchemy(app)

class Users(db.Model):
  __tablename__ = 'Users'
  ID = db.Column(db.Integer, primary_key=True)
  displayName = db.Column(db.String(16), nullable=False)
  firstName = db.Column(db.String(25), nullable=False)
  lastName = db.Column(db.String(25), nullable=False)

  def json(self):
    return {'displayName': self.displayName, 'firstName': self.firstName, 'lastName': self.lastName, 'ID': self.ID}
  
  def create_user(_displayName, _firstName, _lastName):
    new_user = Users(displayName=_displayName, firstName=_firstName, lastName=_lastName)
    db.session.add(new_user)
    db.session.commit()

  def get_all_users():
    all_users = []
    for e in Users.query.all():
      all_users.append(Users.json(e))
    return all_users

  def get_user_by_string(_query):
    return Users.query.filter((Users.displayName == _query) | (Users.firstName == _query) | (Users.lastName == _query)).first()

  def get_user_by_id(_ID):
    return Users.query.filter_by(ID=_ID).first()

  def __repr__(self):
    user_object = {
      'displayName': self.displayName,
      'firstName': self.firstName,
      'lastName': self.lastName,
      'ID': self.ID,
      }
    return json.dumps(user_object)
 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from ENV import app

db = SQLAlchemy(app)

class Users(db.Model):
  __tablename__ = 'Users'
  ID = db.Column(db.Integer, primary_key=True)
  DisplayName = db.Column(db.String(16), nullable=False)
  FirstName = db.Column(db.String(25), nullable=False)
  LastName = db.Column(db.String(25), nullable=False)
  UserName = db.Column(db.String(25), nullable=False)
  Password = db.Column(db.String(80), nullable=False)

  def json(self):
    return {
      'DisplayName': self.DisplayName,
      'FirstName': self.FirstName,
      'LastName': self.LastName,
      'UserName': self.UserName,
      'Password': self.Password,
      'ID': self.ID
      }
  
  def create_user(_userName, _password, _displayName, _firstName, _lastName):
    new_user = Users(UserName=_userName, Password=_password, DisplayName=_displayName, FirstName=_firstName, LastName=_lastName)
    db.session.add(new_user)
    db.session.commit()

  def delete_user(_ID):
    Users.query.filter_by(ID=_ID).delete()
    db.session.commit()
    return 'Success!'

  def get_all_users():
    all_users = []
    for e in Users.query.all():
      all_users.append(Users.json(e))
    return all_users

  def get_user_by_string(_query):
    return Users.query.filter((Users.DisplayName == _query) | (Users.FirstName == _query) | (Users.LastName == _query)).first()

  def get_user_by_id(_ID):
    return Users.query.filter_by(ID=_ID).first()

  def __repr__(self):
    return str({
      'displayName': self.DisplayName,
      'firstName': self.FirstName,
      'lastName': self.LastName,
      'userName': self.UserName,
      'password': self.Password,
      'ID': self.ID,
    })

  def username_password_match(_userName, _password):
    user = Users.query.filter_by(UserName=_userName).filter_by(Password=_password).first()
    if user is None:
      return False
    else:
      return True
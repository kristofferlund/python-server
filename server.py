from flask import Flask, jsonify, request, abort, Response
from ENV import *
from models.UserModel import *
from models.RoomModel import *

import json

@app.route("/")
def main():
    print('App started')

def validUserObject(userObject):
    if ("DisplayName" in userObject and "FirstName" in userObject and "LastName" in userObject):
        return True
    else:
        return False

# Create new user
@app.route("/users", methods=["POST"])
def create_user():
    request_data = request.get_json()
    if(validUserObject(request_data)):
        Users.create_user(request_data['DisplayName'], request_data['FirstName'], request_data['LastName'])
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/Users/" + (str(request_data['DisplayName']) + str(request_data['FirstName']) + str(request_data['LastName']))
        return response
    else:
        invalidRoomObjectErrorMsg = {
            "error": "Invalid object passed in request"
        }
        response = Response(json.dumps(invalidRoomObjectErrorMsg), status=400, mimetype='application/json')
        return response

# Get all users
@app.route("/users")
def get_all_users():
    # Returns list of users
    return jsonify({'users': Users.get_all_users()})

@app.route("/users", methods=["DELETE"])
def delete_user():
    request_data = request.get_json()
    Users.delete_user(request_data["ID"])

@app.route("/users/<query>")
def get_user_by_string(query):
    return str(Users.get_user_by_string(query))

@app.route("/users/<int:ID>")
def get_user_by_id(ID):
    # Returns user object
    return str(Users.get_user_by_id(ID))

def validRoomObject(roomObject):
    if "RoomName" in roomObject:
        return True
    else:
        return False

# Add room
@app.route("/rooms", methods=["POST"])
def add_room():
    request_data = request.get_json()
    if(validRoomObject(request_data)):
        Rooms.create_room(request_data['RoomName'])
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/Rooms/" + str(request_data["RoomName"])
        return response
    else:
        invalidRoomObjectErrorMsg = {
            "error": "Invalid object passed in request",
        }
        response = Response(json.dumps(invalidRoomObjectErrorMsg), status=400, mimetype='application/json')
        return response

@app.route("/rooms", methods=["DELETE"])
def delete_room():
    request_data = request.get_json()
    Rooms.delete_room(request_data["ID"])

@app.route("/rooms")
def get_all_rooms():
    return jsonify({'rooms': Rooms.get_all_rooms()})

@app.route("/rooms/<query>")
def get_room_by_string(query):
    return str(Rooms.get_room_by_string(query))

@app.route("/rooms/<int:ID>")
def get_room_by_id(ID):
    return str(Rooms.get_room_by_id(ID))


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 80)
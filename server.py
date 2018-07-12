from flask import Flask, jsonify, request, abort
from ENV import *
from UserModel import *

import json

@app.route("/")
def main():
    print ("SUH DUDE")
    return 'Jada'

# Create new user
@app.route("/users", methods=["POST"])
def create_user():
    request_date = request.get_json()
    Users.create_user(request_data['displayName'], request_data['firstName'], request_data['lastName'])


# Get all users
@app.route("/users")
def get_all():
    # Returns list of users
    return jsonify({'users': Users.get_all_users()})

@app.route("/users/<query>")
def get_user_by_string(query):
    return str(Users.get_user_by_string(query))

@app.route("/users/<int:ID>")
def get_user_by_id(ID):
    # Returns user object
    return str(Users.get_user_by_id(ID))

# Add room
#@app.route("/books", methods=["POST"])
#def add_room():
#    return jsonify(request.get_json())

# Get room
#@app.route("/room", methods=["GET"])
#def get_room_by_id():
#    roomId = request.args.get('ID')
#    row = cursor.execute("SELECT * FROM Rooms WHERE ID = %s" % roomId).fetchone()
#    if row:
#        return str(row) # Tupple format
#    else:
#        print ('There was no room to be found')
#        abort(404)


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 80)
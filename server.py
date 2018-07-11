from ENV import *
from flask import Flask, jsonify, request, abort
import json
from UserModel import *

@app.route("/")
def main():
    print ("SUH DUDE")
    return 'Jada'

# Create new user
@app.route("/users", methods=["POST"])
def create_user():
    request_date = request.get_json()
    Users.create_user(request_data['displayName'], request_data['firstName'], request_data['lastName'])


# Get user
@app.route("/users", methods=["GET"])
def get_all():
    return jsonify({'users': Users.get_all_users()})

#def get_user_by_dn():
#    display_name = request.args.get('DisplayName')
#    print ("Looking for a user")
#    row = cursor.execute("SELECT * FROM Users WHERE DisplayName = '%s" % str(display_name) +"'").fetchone()
#    if row:
 #       return str(row)
#    else:
#        print ('No user with this DN')

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
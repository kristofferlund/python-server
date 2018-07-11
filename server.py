import json
import getpass
import pyodbc
from ENV import *
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

server = SERVER_NAME
# username = input("Input server username: ")
username = SERVER_ADMIN_USR
# password = getpass.getpass("Input server password: ")
password = SERVER_ADMIN_PWD
database = DB_NAME
driver = "{odbc driver 13 for sql server}"
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

@app.route("/")
def main():
    return "Welcome to this nasty server"

# Create new user
@app.route("/user", methods=["POST"])
def add_user():
    print ("Detected request against user")
    username = request.json['username']
    email = request.json['email']

    new_user = User(username, email)
    print (User)

# Get user
@app.route("/user", methods=["GET"])
def get_user_by_id():
    SQLCommand = ("SELECT")
    print ("Looking for a user")
    username = request.json['username']
    id = request.json['chatterId']

# Add room
@app.route("/books", methods=["POST"])
def add_room():
    return jsonify(request.get_json())

# Get room
@app.route("/room", methods=["GET"])
def get_room_by_id():
    roomId = request.args.get('roomId')
    row = cursor.execute("select * from dbo.Rooms where roomId = " + roomId).fetchone()
    if row:
        return jsonify({'room': row.roomId})
        #return str(row)
    else:
        print ('There was no room to be found')
        abort(404)


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 80)
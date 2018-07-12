from flask import Flask
import pyodbc
from flask_sqlalchemy import SQLAlchemy
import urllib

app = Flask(__name__)

SERVER_NAME = ""
SERVER_ADMIN_USR = ""
SERVER_ADMIN_PWD = ""
DB_NAME = ""
SQL_DRIVER = "{odbc driver 13 for sql server}"
CONNECTION_STRING = urllib.parse.quote_plus("DRIVER=%s;SERVER=%s,1433;Database=%s;Uid=%s;Pwd={%s};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;" % (SQL_DRIVER, SERVER_NAME, DB_NAME, SERVER_ADMIN_USR, SERVER_ADMIN_PWD))

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
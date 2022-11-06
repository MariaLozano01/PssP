from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

mysql_hostname = os.getenv("MYSQL_HOSTNAME")
mysql_username = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")

db = SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://' + mysql_username + ':' + mysql_password + '@' + mysql_hostname + ':3306/patients'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #allows us to save changes done to the database and input them into a file
app.secret_key = '343fdksjf34#$#dfjkhdf0SDJH0df9fd98343fdfu34rf' #Allows that when flask starts a new instance that it has a unique identifier so we don't
#get an error on SQLAlchemy 

db.init_app(app)

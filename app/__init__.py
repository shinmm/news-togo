from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#sql-alchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#create the database
db.create_all()

from app import routes
from app.models import *

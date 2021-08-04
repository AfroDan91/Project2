from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('database_uri'))

app.config['SECRET_KEY'] = str(os.getenv('secret_key'))

db = SQLAlchemy(app)

from . import routes
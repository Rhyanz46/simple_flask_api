from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route('/')
def index():
    return 'index root'
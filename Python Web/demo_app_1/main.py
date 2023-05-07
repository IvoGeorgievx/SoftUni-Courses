from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres-user: password @localhost:5432/complain_app'

db = SQLAlchemy(app)
api = Api(app)

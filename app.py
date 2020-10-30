import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app_config import config

# drop the database before starting
db_file = config.get_db_file()
os.remove(db_file)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file
api = Api(app)
db = SQLAlchemy(app)

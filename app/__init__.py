from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
from app import routes






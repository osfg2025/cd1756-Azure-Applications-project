"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session


app = Flask(__name__)
app.config.from_object(Config)
# Add any logging levels and handlers with app.logger
# Setting logging level to info
app.logger.setLevel(logging.INFO)
# Creating stream handler for logging
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
# Adding handler to app.logger object
app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views

import FlaskWebProject.views

###
# Imports
###
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os


###
# App config
###
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.secret_key = "blah"
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint

# Register Our BluePrint
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)

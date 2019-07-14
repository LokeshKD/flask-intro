###
# Imports
###
from flask import Flask, flash, redirect, session, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import os


###
# App config
###
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.secret_key = "blah"
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

# Register Our BluePrint
app.register_blueprint(users_blueprint)


###
# Helper Functions
###

#login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

###
# Routes
###

@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

###
# Run Server
###

if __name__ == '__main__':
    app.run()

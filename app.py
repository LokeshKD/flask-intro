from flask import Flask, render_template, request
from flask import url_for, redirect, session, flash, g
from flask_bcrypt import Bcrypt
# This is when moving from dealing with direct db to ORM.
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
#import sqlite3


app = Flask(__name__)
bcrypt = Bcrypt(app)
#Config
# From config.py
#app.config.from_object('config.DevConfig')
#app.config.from_object('config.ProdConfig')
import os
app.config.from_object(os.environ['APP_SETTINGS'])

app.secret_key = "blah"

db = SQLAlchemy(app)

from models import BlogPost

#login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    #return "Hello World!"
    '''
    g.db = db_connect()  #this is flask temp object; ie. "g"
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    '''
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid Credentials."
        else:
            session['logged_in'] = True
            flash('You were just logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out')
    return redirect(url_for('welcome'))

#def db_connect():
#    return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run()

###
# Imports
###
from project import app, db
from project.models import BlogPost
from project.home.forms import MessageForm
from flask import render_template, Blueprint, flash, url_for, redirect, request
from flask_login import login_required, current_user

###
# Config
###

home_blueprint = Blueprint('home', __name__,
                        template_folder = 'templates')

###
# Helper Functions
###
'''
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap
'''
###
# Routes
###

# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])   # pragma: no cover
@login_required   # pragma: no cover
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template(
            'index.html', posts=posts, form=form, error=error)

@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')

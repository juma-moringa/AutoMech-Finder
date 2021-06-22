from . import main
from flask import render_template,request,redirect,url_for,abort, flash
from flask_login import login_required, current_user
from ..models import User
from .. import db,photos

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
  
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

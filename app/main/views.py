
from werkzeug.utils import format_string
from app import main
from flask.helpers import flash
from . import main
from .. import db
from ..models import Mech, User
from flask_login import login_required, current_user
from datetime import datetime
# from ..request import get_quote
from sqlalchemy.sql import text
from ..email import mail_message
from app import models
from flask import render_template,request,redirect,url_for,abort, flash
from .. import db,photos
from .forms import UpdateProfile




@main.route("/", methods=["GET", "POST"])
def index():

    title = 'AutoMech'

    return render_template('index.html', title=title)


@main.route('/mech')
def viewmech():

    all_mechs = Mech.query.order_by('id').all()

    title = 'AutoMech'
    
    return render_template('viewmech.html', title=title, mech=all_mechs)



  



@main.route('/user/<uname>')
def user_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)


    return render_template("profile/user_profile.html", user = user)

@main.route('/mech/<uname>')
def mech_profile(uname):
    mech = Mech.query.filter_by(username = uname).first()

    if mech is None:
        abort(404)

    return render_template("profile/mech_profile.html", mech = mech)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_user_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.user_profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/mech/<uname>/update',methods = ['GET','POST'])
@login_required
def update_mech_profile(uname):
    mech = Mech.query.filter_by(username = uname).first()
    if mech is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        mech.bio = form.bio.data
        mech.specialization = form.specialization.data
        mech.location= form.location.data
        db.session.add(mech)
        db.session.commit()

        return redirect(url_for('.mech_profile',uname=mech.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.user_profile',uname=uname))

@main.route('/mech/<uname>/updatemech/pic',methods= ['POST'])
@login_required
def update_mech_pic(uname):
    mech = Mech.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        mech.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.mech_profile',uname=uname))




@main.route('/search', methods=['GET', 'POST'])
def search():
    '''
    View function to display the search results
    '''
    item = request.form['service_query'].lower()
    location = request.form['location_query'].lower()
    username = request.form['mech_query'].lower()
    spec =[]
    spec = Mech.get_mech(item) or Mech.get_mech2(location) or Mech.get_mech3(username)

    return render_template('display.html', spec= spec)


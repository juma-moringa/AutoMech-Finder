from . import main
from flask import render_template,request,redirect,url_for,abort, flash
from flask_login import login_required, current_user
from ..models import Mech, User
from .. import db,photos
from .forms import UpdateProfile


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
  
    return render_template('index.html')

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

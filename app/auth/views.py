from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from ..models import Mech, User
from .forms import LoginForm, LoginForm2, RegistrationForm, RegistrationForm2
from .. import db
from ..email import mail_message
from .import auth


# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')
    title = "AutoMech login"
    return render_template('auth/login.html', login_form=login_form, title=title)


# register route
@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to AutoMech",
                     "email/welcome_user", user.email, user=user)
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html', registration_form=form)


# logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


#####################################################################################################################################
#################################################################################################################################
  # Login route
# @auth.route('/loginmech', methods=['GET', 'POST'])
# def loginmech():
#     mechlogin_form = LoginForm2()
#     if mechlogin_form.validate_on_submit():
#         mech = Mech.query.filter_by(email=mechlogin_form.email.data).first()
#         if mech is not None and mech.verify_password(mechlogin_form.password.data):
#             login_user(mech, mechlogin_form.remember.data)
#             return redirect(request.args.get('next') or url_for('main.index'))
#         flash('Invalid username or Password')
#     title = "AutoMech login"
#     return render_template('auth/loginmech.html', mechlogin_form=mechlogin_form, title=title)

# register route


@auth.route('/registermech', methods=["GET", "POST"])
def registermech():
    formmech = RegistrationForm2()
    if formmech.validate_on_submit():
        mech = Mech(email=formmech.email.data,
                    username=formmech.username.data, password=formmech.password.data)
        db.session.add(mech)
        db.session.commit()
        mail_message("Welcome to AutoMech",
                     "email/welcome_user", mech.email, mech=mech)

        return redirect(url_for('main.index'))

    title = "New Account"
    return render_template('auth/registermech.html', registration_form2=formmech)
    


# logout route
@auth.route('/logout')
@login_required
def logoutmech():
    logout_user()
    return redirect(url_for("main.index"))

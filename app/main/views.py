from flask import render_template, request, redirect, url_for
from flask.helpers import flash
from . import main
from .. import db
from ..models import User
from flask_login import login_required, current_user
from datetime import datetime
# from ..request import get_quote
from ..email import mail_message


# 1 the main index(default)
@main.route("/", methods=["GET", "POST"])
def views():

       

        return render_template("index.html")

from app import main
from flask import render_template, request, redirect, url_for
from . import main


@main.route('/')
def index():
    title = 'AutoMech'


    return render_template('viewmech.html', title=title)

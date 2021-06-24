from werkzeug.utils import format_string
from app import main
from flask import render_template, request, redirect, url_for
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


@main.route("/", methods=["GET", "POST"])
def index():

    title = 'AutoMech'

    return render_template('index.html', title=title)


@main.route('/mech')
def viewmech():

    all_mechs = Mech.query.order_by('id').all()

    title = 'AutoMech'

    return render_template('viewmech.html', title=title, mech=all_mechs)


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


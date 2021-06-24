from app.main.forms import queriesForm
from flask import render_template, request, redirect, url_for
from flask.helpers import flash
from . import main
from .. import db
from ..models import User, Formfield
from flask_login import login_required, current_user
from datetime import datetime
# from ..request import get_quote
from ..email import mail_message


# 1 the main index(default)
@main.route("/", methods=["GET", "POST"])
def index():

       

        return render_template("index.html")



@main.route('/queries',methods = ['GET' , 'POST'])
def queries():
    queries_form = queriesForm()
    if  queries_form.validate_on_submit():
        problem = queries_form.problem.data
        new_queries = Formfield(query=problem)
        new_queries.save_queries()
    return render_template('queries.html',queries_form = queries_form)

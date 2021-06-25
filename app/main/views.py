from app.main.forms import queriesForm
from flask import render_template, request, redirect, url_for
from flask.helpers import flash
from . import main
from .. import db
from ..models import User, Formfield,Display
from flask_login import login_required, current_user
from datetime import datetime
# from ..request import get_quote
from ..email import mail_message


# 1 the main index(default)
@main.route("/", methods=["GET", "POST"])
def index():

       

        return render_template('index.html')

# @main.route('/',methods = ['GET' , 'POST'])
# def queries():
#         queries = Formfield()

#         return  render_template('queries.html',queries=queries)











@main.route('/newqueries',methods = ['GET' , 'POST'])
def new_query():

    queries_form = queriesForm()
    if  queries_form.validate_on_submit():
        query = queries_form.query.data
        new_query = Formfield(query=query)
        db.session.add(new_query)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('new_queries.html',queries_form = queries_form)


@main.route("/display/<int:id>", methods = ["POST", "GET"])
def Displayqueries(formfield_id):
    formfield = Formfield.filter_by(formfield_id=formfield_id).all()
    display = Display.query.filter_by(post_id=formfield_id).all()
    queries_Form= queriesForm()
    if queries_Form.validate_on_submit():
        display = queries_Form.problem.data
        new_query = Display(post_id=formfield_id,display=display)
        new_query.save_display()
    return render_template('display_queries.html', formfield=formfield, display=display, queries_Form=queries_Form)

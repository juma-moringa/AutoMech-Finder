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
def index():

       

        return render_template("index.html")



@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def queries():
    """ 
    Function to add a defect 
    """


    return redirect("index.html")

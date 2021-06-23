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
def queries(id):
    """ 
    Function to post comments 
    """
    
    form = CommentForm()
    title = 'post comment'
    pitches = Pitch.query.filter_by(id=id).first()

    if pitches is None:
         abort(404)

    if form.validate_on_submit():
        opinion = form.opinion.data
        new_comment = Comments(opinion = opinion, user_id = current_user.id, pitches_id = pitches.id)
        new_comment.save_comment()
        return redirect(url_for('.view_pitch', id = pitches.id))


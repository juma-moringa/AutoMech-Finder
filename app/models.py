from . import db
from flask_login import login_manager

@login_manager.user_loader
def load_user(user_id):
    return (int(user_id))

class Formfield(db.Model):

    __tablename__ = 'formfields'

    id = db.Column(db.Integer, primary_key = True)
    form_id = db.Column(db.Integer, db.ForeignKey('formbooking.id'))
    label = db.Column(db.String(80))
    placeholder_text = db.Column(db.String(80))
    help_text = db.Column(db.String(500))
    box_checked = db.Column(db.Boolean, nullable = True, default = False)
    options = db.Column(db.String) 
    answer = db.Column(db.String)
    required = db.Column(db.Boolean, nullable = False, default = False)
    order = db.Column(db.Integer)
    fieldtype = db.Column(db.Integer)
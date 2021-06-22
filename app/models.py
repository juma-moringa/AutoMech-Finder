from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class Formfield(db.Model):
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
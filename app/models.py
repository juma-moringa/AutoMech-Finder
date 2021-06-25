
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# user class
class User(UserMixin,db.Model):

    '''
    User class to define user Objects
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    #ROLES
    # is_active = db.Column(db.Boolean,default=False)
    # urole = db.Column(db.String(80))


    
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    # def get_id(self):
    #         return self.id
    # def is_active(self):
    #         return self.is_active
    # def activate_user(self):
    #         self.is_active = True         
    # def get_username(self):
    #         return self.username
    # def get_urole(self):
            # return self.urole

    def __repr__(self):
        return f'User {self.username}'



class Mech(UserMixin,db.Model):

    '''
    Mechanics class to define mechanic Objects
    '''
    __tablename__ = 'mechanics'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # password_hash = db.Column(db.String(255))
    role = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    specialization = db.Column(db.String(255), index = True,nullable = False)
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'Mech {self.username}'


class Formfield(db.Model):
    __tablename__ = 'formfields'
    id = db.Column(db.Integer, primary_key = True)
    query = db.Column(db.String(255))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_queries(self):
        """
        Save the queries
        """
        db.session.add(self)
        db.session.commit()

    # @classmethod
    # def get_queries(id):
    #     queries = Formfield.query.filter_by(post_id=id).all()
    #     return queries



class Display(db.Model):
    __tablename__ = "displays"

    id = db.Column(db.Integer, primary_key = True)
    display = db.Column(db.String)
    dispalyed_at = db.Column(db.DateTime)
    dispalyed_by = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    formfield_id = db.column(db.Integer, db.ForeignKey("formfield_id"))

    def save_display(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_comments(cls, id):
        display= Display.query.filter_by(formfield_id = id).all()
        return display

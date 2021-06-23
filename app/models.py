
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

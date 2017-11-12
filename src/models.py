from werkzeug.security import generate_password_hash, check_password_hash

from exts import db
import datetime


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    telephone = db.Column(db.String(11),nullable=False)
    _password = db.Column(db.String(100),nullable=False)

    def __init__(self,*args,**kwargs):
        password = kwargs.pop('password')
        username = kwargs.pop('username')
        telephone = kwargs.pop('telephone')
        self.password = password
        self.username = username
        self.telephone = telephone

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,rawpwd):
        self._password = generate_password_hash(rawpwd)

    def check_password(self,rawpwd):
        return check_password_hash(self._password,rawpwd)


class ScheduleRecordModel(db.Model):
    __tablename__ = 'scheduleRecord'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    phone = db.Column(db.String(11),nullable=False)
    childname = db.Column(db.String(32),nullable=False)
    childage = db.Column(db.Integer,nullable=False)
    udate = db.Column(db.DateTime,default=datetime.datetime.now)
    cdate = db.Column(db.DateTime, default=datetime.datetime.now)
    note = db.Column(db.Text, nullable=True)
    # course_id = db.Column(db.String(64),db.ForeignKey('course.id'))
    # course = db.relationship('CourseModel')

class CourseModel(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    name = db.Column(db.String(32),nullable=False)
    discription = db.Column(db.Text,nullable=False)
    img_url = db.Column(db.String(128),nullable=True)
    cdate = db.Column(db.DateTime, default=datetime.datetime.now)
    udate = db.Column(db.DateTime, default=datetime.datetime.now)





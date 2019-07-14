from setting import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'users'
    key = db.Column(db.Integer, primary_key=True, autoincrement = True)
    id = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    #active_state = db.Column(db.Boolean, default=True)
    address = db.Column(db.String(64))
    discount = db.Column(db.String(64))
    credit = db.Column(db.Integer, default=0)
    jewelry = db.relationship('Jewelrys', backref='users',lazy='dynamic')

class Jewelrys(db.Model):
    __tablename__ = 'jewelrys'
    key = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    size = db.Column(db.String(64), default=0)
    price = db.Column(db.String(64), default=0)
    credit = db.Column(db.Integer, default=0)
    catagory = db.Column(db.String(64))
    image = db.Column(db.Text, nullable=True)
    status = db.Column(db.Boolean, default=True)
    uid = db.Column(db.String(64), db.ForeignKey("users.id", ondelete='cascade'))
    #csid = db.Column(db.String(50), db.ForeignKey("category.name", ondelete='cascade'))

class Jewelrys_Photos(db.Model):
    __tablename__ = 'jewelry_info'
    key = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(64))
    image = db.Column(db.Text(64), nullable=True)

class Coupon(db.Model):
    __tablename__ = "coupon"
    key = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    active_state = db.Column(db.Boolean, default=True)
    create_date = db.Column(db.DateTime, default=datetime.now)
    use_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    user_name = db.Column(db.String(64))
    user_phone = db.Column(db.Integer, default=0)
    used = db.Column(db.Boolean, default=False)

class Questions(db.Model):
    __tablename__="questions"
    id = db.Column(db.Integer, default=1)
    question = db.Column(db.String(64), primary_key=True)
    select1 = db.Column(db.String(64))
    select2 = db.Column(db.String(64))
    select3 = db.Column(db.String(64))
    select4 = db.Column(db.String(64))

class Results(db.Model):
    __tablename__="results"
    question = db.Column(db.String(64), primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.now)
    select1 = db.Column(db.String(64))
    select2 = db.Column(db.String(64))
    select3 = db.Column(db.String(64))
    select4 = db.Column(db.String(64))
    count_select1 = db.Column(db.Integer, default=0)
    count_select2 = db.Column(db.Integer, default=0)
    count_select3 = db.Column(db.Integer, default=0)
    count_select4 = db.Column(db.Integer, default=0)

#coupon1 = Coupon(id='123hjh')
#db.session.add(coupon1)
#db.session.commit()

db.create_all()


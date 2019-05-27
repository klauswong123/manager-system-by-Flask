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

class Category(db.Model):
    __tablename__ = 'category'
    key = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    #jewelry = db.relationship('Jewelrys', backref='catagory', lazy='dynamic')

class Coupon(db.Model):
    __tablename__ = "coupon"
    key = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(64), unique=True)
    active_state = db.Column(db.Boolean, default=True)
    create_date = db.Column(db.DateTime, default=datetime.now)
    use_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    user_name = db.Column(db.String(64), unique=True)
    user_phone = db.Column(db.Integer, default=0)

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




'''class Photo(db.Model):
    __tablename__ = "photo"
    key = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.String(64))
    name = db.Column(db.String(64), unique=True)'''
#coupon1 = Coupon(id='123hjh')
#db.session.add(coupon1)
#db.session.commit()
#db.drop_all()
db.create_all()


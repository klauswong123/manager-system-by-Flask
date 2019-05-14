from setting import db,app
from datetime import datetime

db.init_app(app)

class Users(db.Model):
    __tablename__ = 'users'
    key = db.Column(db.Integer, primary_key=True, autoincrement = True)
    id = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    #active_state = db.Column(db.Boolean, default=True)
    address = db.Column(db.String(64))
    discount = db.Column(db.String(64))
    credit = db.Column(db.Integer, default=0)

class Coupon(db.Model):
    __tablename__ = "coupon"
    key = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(64), unique=True)
    active_state = db.Column(db.Boolean, default=True)
    create_date = db.Column(db.DateTime, default=datetime.now)
    use_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    user_name = db.Column(db.String(64), unique=True)
    user_phone = db.Column(db.Integer, default=0)

#coupon1 = Coupon(id='123hjh')
#db.session.add(coupon1)
#db.session.commit()
#db.drop_all()
db.create_all()


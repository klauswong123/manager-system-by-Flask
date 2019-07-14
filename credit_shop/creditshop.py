from flask import Blueprint, session, render_template, flash, redirect, url_for
from models import Users, Jewelrys
from setting import db
from models import Coupon
credit = Blueprint('creditshop', __name__, url_prefix='/credit_shop' ,template_folder='templates',static_folder='.static')

@credit.route('/')
def credit_shop():
    if session.get('user_id') is None:
        flash("未登录")
        return redirect(url_for('login'))
    user = Users.query.filter_by(id=session.get('user_id')).first()
    jewelrys = []
    jewelrys.append(Jewelrys.query.filter_by(image='file1.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='file2.jpg,', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='file3.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='file4.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='file5.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='file6.jpg', status=True).first())
    number = []
    number.append(int(Jewelrys.query.filter_by(image='file1.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='file2.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='file3.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='file4.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='file5.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='file6.jpg', status=True).count()))
    return render_template('credit_shop.html', user=user, jewelry=jewelrys, number=number)

@credit.route('/goods', methods=['GET','POST'])
def exchange_goods():
    if session.get('user_id') is None:
        flash("未登录")
        return redirect(url_for('login'))
    user = Users.query.filter_by(id=session.get('user_id')).first()
    jewelry = user.jewelry
    coupons = Coupon.query.filter_by(user_name=session.get('user_id'))
    return render_template('credit_goods.html',jewelry=jewelry,coupons=coupons,user=1)

@credit.route('/use_credit/<string:file>', methods=['GET','POST'])
def use_credit(file):
    if session.get('user_id') is None:
        flash("未登录")
        return redirect(url_for('login'))
    jewelry = Jewelrys.query.filter_by(image=file, status=True).first()
    user = Users.query.filter_by(id=session.get('user_id')).first()
    if jewelry:
        user.credit = (int(user.credit)-int(jewelry.credit))
        user.jewelry.append(jewelry)
        jewelry.status = False
        db.session.add(user)
    return redirect(url_for('creditshop.credit_shop'))


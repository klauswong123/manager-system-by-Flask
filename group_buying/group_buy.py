'''from flask import Blueprint, session, render_template, flash, redirect, url_for
from models import Users, Jewelrys, Jewelrys_Photos
from setting import db
group = Blueprint('group_buy', __name__, url_prefix='/group_buy' ,template_folder='templates',static_folder='.static')

@group.route('/')
def group_shop():
    user = Users.query.filter_by(id=session.get('user_id')).first()
    jewelrys = []
    jewelrys.append(Jewelrys.query.filter_by(image='group1.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='group2.jpg,', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='group3.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='group4.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='group5.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='group6.jpg', status=True).first())
    number = []
    number.append(int(Jewelrys.query.filter_by(image='group1.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='group2.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='group3.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='group4.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='group5.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='group6.jpg', status=True).count()))
    return render_template('credit_shop.html', user=user, jewelry=jewelrys, number=number)

@group.route('/goods', methods=['GET','POST'])
def group_goods():
    if session.get('user_id') is None:
        flash("未登录")
        return redirect(url_for('login'))
    user = Users.query.filter_by(id=session.get('user_id')).first()
    jewelry = user.jewelry
    return render_template('credit_goods.html',jewelry=jewelry,user=1)

@group.route('/details/<string:file>', methods=['GET','POST'])
def use_credit(file):
    if session.get('user_id') is None:
        flash("未登录")
        return redirect(url_for('login'))
    jewelry = Jewelrys.query.filter_by(image=file, status=True).first()
    photos = Jewelrys_Photos.query.filter_by(name=jewelry.name)
    number = photos.count()
    return render_template('photos.html', photos=photos, number=number)'''
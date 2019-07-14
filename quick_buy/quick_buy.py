'''from flask import Blueprint, session, render_template, flash, redirect, url_for
from models import Users, Jewelrys
from setting import db
quick = Blueprint('quick_buy', __name__, url_prefix='/quick_buy' ,template_folder='templates',static_folder='.static')

@quick.route('/')
def quick_shop():
    user = Users.query.filter_by(id=session.get('user_id')).first()
    jewelrys = []
    jewelrys.append(Jewelrys.query.filter_by(image='quick1.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='quick2.jpg,', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='quick3.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='quick4.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='quick5.jpg', status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='quick6.jpg', status=True).first())
    number = []
    number.append(int(Jewelrys.query.filter_by(image='quick1.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='quick2.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='quick3.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='quick4.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='quick5.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='quick6.jpg', status=True).count()))
    return render_template('quick_shop.html', user=user, jewelry=jewelrys, number=number)

@quick.route('/goods', methods=['GET','POST'])
def quick_goods():
    if session.get('user_id') is None:
        flash("未登录")
        return redirect(url_for('login'))
    user = Users.query.filter_by(id=session.get('user_id')).first()
    jewelry = user.jewelry
    return render_template('quick_goods.html',jewelry=jewelry,user=1)

@quick.route('/use_credit/<string:file>', methods=['GET','POST'])
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
    return redirect(url_for('quick_buy.quick_shop'))'''
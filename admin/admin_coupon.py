from flask import Blueprint, session, render_template, flash, redirect, url_for,abort,request, jsonify
from models import Coupon, Questions, Results
from forms import Coupon_CreateForm, Question_CreateForm
from setting import db

admin_coupon = Blueprint('admin_coupon', __name__, url_prefix='/admin/coupon' ,template_folder='templates',static_folder='static')

@admin_coupon.route('/')
def admin_coupon_detail():
    if not session.get('admin'):
        abort(400)
    coupons = Coupon.query.all()
    update_coupon = coupons
    return render_template('admin_coupon.html', coupons=update_coupon)

@admin_coupon.route('/create_coupon', methods=['GET', 'POST'])
def create_coupon():
    if not session.get('admin'):
        abort(400)
    form = Coupon_CreateForm()
    coupons = Coupon.query.all()
    if form.validate_on_submit():
        number = form.number.data
        for i in range(number):
            result = "買100元即減5元（每日每人只可領取一張）"
            coupon = Coupon(name=result, active_state=True)
            db.session.add(coupon)
        flash('增加成功')
        coupons = Coupon.query.all()
        return redirect(url_for('admin_coupon.admin_coupon_detail'))
    return render_template('create_coupon.html', form=form)

@admin_coupon.route('/create_question', methods=['GET', 'POST'])
def create_question():
    if not session.get('admin'):
        abort(400)
    form = Question_CreateForm()
    if form.validate_on_submit():
        question = form.question.data
        select1 = form.select1.data
        select2 = form.select2.data
        select3 = form.select3.data
        select4 = form.select4.data
        if Questions.query.filter_by(id=1).first():
            result = Results(question=question, select1=select1, select2=select2, select3=select3,select4=select4)
            db.session.add(result)
            que = Questions.query.filter_by(id=1).first()
            que.question = question
            que.select1 = select1
            que.select2 = select2
            que.select3 = select3
            que.select4 = select4
            db.session.add(que)
            flash('增加成功')
            return redirect(url_for('admin_coupon.question'))
        else:
            que = Questions(id=1,question=question,select1=select1,select2=select2,select3=select3,select4=select4)
            result = Results(question=question, select1=select1, select2=select2, select3=select3, select4=select4)
            db.session.add(que)
            db.session.add(result)
            flash('增加成功')
            return redirect(url_for('admin_coupon.question'))
    return render_template('create_question.html', form=form)

@admin_coupon.route('/question', methods=['GET', 'POST'])
def question():
    if not session.get('admin'):
        abort(400)
    results = Results.query.all()
    return render_template('admin_question.html', results=results)



from flask import Blueprint, render_template,session, flash, redirect, url_for,request
from models import Coupon,Questions,Results
from setting import db
from datetime import datetime
from forms import AnswerForm
coupon = Blueprint('coupon', __name__, url_prefix='/coupon' ,template_folder='templates',static_folder='.static')

@coupon.route('/')
def coupon_detail():
    if session.get('user_id') is None:
        flash("未登录")
        return redirect(url_for('login'))
    user=True
    coupons = Coupon.query.all()
    update_coupon = coupons[-3:]
    return render_template('coupon.html', coupons=update_coupon, user=user)

@coupon.route('/take', methods=['GET', 'POST'])
def coupon_take():
    if session.get('user_id') is None:
        flash("未登录")
        return redirect(url_for('login'))
    name = session.get('user_id')
    user = True
    if Coupon.query.filter_by(user_name=str(name)):
        coupons = Coupon.query.all()
        for coupon in coupons:
            usedate = coupon.use_date
            used = usedate.strftime("%d-%m-%Y (%H:%M:%S.%f)")
            nowdate = datetime.now()
            nowd = nowdate.strftime("%d-%m-%Y (%H:%M:%S.%f)")
            taked = str(used)[0:11]
            now = str(nowd)[0:11]
            if taked == now:
                flash("今日已經領取，請明日再領")
                return redirect(url_for('coupon.coupon_detail'))
    else:
        return redirect(url_for('coupon.question_take'))
    return redirect(url_for('coupon.coupon_detail'))

@coupon.route('/question', methods=['GET','POST'])
def question_take():
    if session.get('user_id') is None:
        flash("未登录")
        return redirect(url_for('login'))
    form = AnswerForm()
    if form.validate_on_submit():
        que = Questions.query.filter_by(id=1).first()
        result = Results.query.filter_by(question=que.question).first()
        num = form.select.data
        if num == '1':
            result.count_select1 = result.count_select1 + 1
        if num == '2':
            result.count_select2 = result.count_select2 + 1
        if num == '3':
            result.count_select3 = result.count_select3 + 1
        if num == '4':
            result.count_select4 = result.count_select4 + 1
        db.session.add(result)
        cou = Coupon.query.filter_by(active_state=True).first()
        cou.user_name = session.get('user_id')
        cou.active_state = False
        db.session.add(cou)
        return redirect(url_for('coupon.coupon_detail'))
    return render_template('questions.html', form=form, user=True)


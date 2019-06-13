from flask import Blueprint, render_template,session
from models import Coupon
from forms import Coupon_TakeForm
from setting import db

coupon = Blueprint('coupon', __name__, url_prefix='/coupon' ,template_folder='templates',static_folder='.static')

@coupon.route('/')
def coupon_detail():
    if session.get('user_id'):
        user=True
    else:
        user=False
    coupons = Coupon.query.all()
    update_coupon = coupons[-3:]
    return render_template('coupon.html', coupons=update_coupon, user=user)

@coupon.route('/take', methods=['GET', 'POST'])
def coupon_take():
    if session.get('user_id'):
        user=True
    else:
        user=False
    form = Coupon_TakeForm()
    if form.validate_on_submit():
        ig = form.ig.data
        coupon = Coupon.query.filter_by(active_state=True).first()
        coupon.user_name = ig
        coupon.active_state = False
        db.session.add(coupon)
        return render_template('coupon_result.html', coupon=coupon)
    return render_template('take_coupon.html', form=form, user=user)
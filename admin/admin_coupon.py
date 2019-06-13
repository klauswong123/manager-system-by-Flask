from flask import Blueprint, session, render_template, flash, redirect, url_for,abort,request, jsonify
from models import Coupon
from forms import Coupon_CreateForm
from setting import db
import hashlib, string, random

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
            n = ''.join(random.sample(string.ascii_letters + string.digits, 16))
            m = hashlib.md5()
            m.update(n.encode('utf-8'))
            result = m.hexdigest()
            coupon = Coupon(id=result, active_state=True)
            db.session.add(coupon)
        flash('增加成功')
        coupons = Coupon.query.all()
        return redirect(url_for('admin_coupon.admin_coupon_detail'))
    return render_template('create_coupon.html', form=form)
import random
from flask import  render_template, redirect, url_for, flash, abort, session, request, jsonify, send_from_directory
from setting import app, db,bootstrap
from forms import AdminForm,LoginForm,SearchForm,AdminAddForm,Coupon_CreateForm, Coupon_TakeForm
from models import Users,Coupon
from forms import LoginForm
import string
import hashlib
from flask_migrate import Migrate,MigrateCommand, upgrade
from flask_script import Manager
import os
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=['GET', 'POST'])
def login():
	if session.get('user_id') is None:
		form = LoginForm()
		if form.validate_on_submit():
			if Users.query.filter_by(id=form.id.data).first() is None:
				flash("賬號錯誤")
				return redirect(url_for('login'))
			user = Users.query.filter_by(id=form.id.data).first()
			#验证密码是否正确
			if user.password != form.password.data:
				flash("密码錯誤")
				return redirect(url_for('login'))
			#记住登录状态
			session['user_id'] = user.id
			#根据身份重定向
			return redirect('/u/' + str(user.id))
		return render_template('form.html', form=form)
	else:
		id = session.get('user_id')
		return redirect('/u/' + str(id))

@app.route('/logout')
def logout():
	if session.get('admin'):
		session['admin'] = None
	#普通用户退出
	elif session.get('user_id') is None:
		flash("未登录")
		return redirect(url_for('login'))
	flash("退出成功")
	session['user_id'] = None
	return redirect(url_for('login'))

@app.route('/u/<string:id>')
def user(id):
	#验证是否已登录
	if session.get('user_id') is None or id!=session.get('user_id'):
		session['user_id'] = None
		flash("未登录")
		return redirect(url_for('login'))
	user = Users.query.filter_by(id=id).first()
	#验证身份
	return render_template('user.html', user=user)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	form = AdminForm()
	if form.validate_on_submit():
		session['admin'] = True
		return redirect('/admin/control')
	return render_template('form.html', form=form)

@app.route('/admin/search', methods=['GET', 'POST'])
def search():
    if not session.get('admin'):
        abort(400)
    form = SearchForm()
    hide = set()
    users = Users.query.all()
    if form.validate_on_submit():
        for user in users:
            word = str('{name}'.format(name=user.id))
            if str(form.keyword.data) not in word:
                hide.add(user)
    return render_template('adminadd.html', form=form, search=True, users=users, hide=hide)


@app.route('/admin/change', methods=['POST'])
def change():
    if not session.get('admin'):
        abort(400)
    user = Users.query.filter_by(key=request.form.get('key')).first()
    user.id = request.form.get('id')
    user.password = request.form.get('password')
    user.credit = request.form.get('credit')
    db.session.add(user)
    return jsonify({'result': 'success'})

@app.route('/coupon')
def coupon_detail():
	coupons = Coupon.query.all()
	update_coupon = coupons[-3:]
	return render_template('coupon.html', coupons=update_coupon)


@app.route('/coupon/take', methods=['GET','POST'])
def coupon_take():
	form = Coupon_TakeForm()
	if form.validate_on_submit():
		phone = form.phone.data
		coupon = Coupon.query.filter_by(active_state=True).first()
		coupon.user_phone = int(phone)
		coupon.active_state = False
		db.session.add(coupon)
		return render_template('coupon_result.html', coupon=coupon)
	return render_template('take_coupon.html', form=form)


@app.route('/admin/coupon')
def admin_coupon():
	if not session.get('admin'):
		abort(400)
	coupons = Coupon.query.all()
	update_coupon = coupons
	return render_template('admin_coupon.html', coupons=update_coupon)

@app.route('/admin/create_coupon', methods=['GET','POST'])
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
		return redirect(url_for('admin_coupon'))
	return render_template('create_coupon.html', form=form)


#管理员控制台路由控制
@app.route('/admin/control', methods=['GET', 'POST'])
def control():
	if not session.get('admin'):
		abort(400)
	users = Users.query.all()
	if request.method == 'POST':
		if request.files['file']:
			file = request.files['file']
			if file.filename == '':
				flash('No selected file')
				return url_for(control)
			if file and allowed_file(file.filename):
				new_filename = '321.jpg'
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
				flash("上傳成功")
	return render_template('control.html', users=users, admin=True)

#管理员新增用户路由控制
@app.route('/admin/add', methods=['GET', 'POST'])
def admin_add():
	if not session.get('admin'):
		abort(400)
	form = AdminAddForm()
	if form.validate_on_submit():
		user = Users(id=form.id.data, password=form.password.data)
		db.session.add(user)
		flash('增加成功')
		return redirect(url_for('control'))
	return render_template('adminadd.html', form=form)


#管理员删除用户路由控制
@app.route('/admin/delete', methods=['POST'])
def admin_delete():
	if session.get('admin'):
		user = Users.query.filter_by(id=request.form.get('id')).first()
		if user:
			db.session.delete(user)
		return 'ok'
	abort(400)

#管理员解冻用户路由控制
@app.route('/admin/normal', methods=['POST'])
def admin_normal():
	if session.get('admin'):
		user = Users.query.filter_by(id=request.form.get('id')).first()
		user.frozen = False
		db.session.add(user)
		return 'ok'
	abort(400)

#错误页面路由控制
@app.errorhandler(404)
def page_not_found(e):
	return render_template('error.html', code='404'), 404


@app.errorhandler(500)
def internal_server_error(e):
	return render_template('error.html', code='500'), 500

@app.errorhandler(400)
def bad_request(e):
	return render_template('error.html', code='400'), 500

@app.route('/download/<path:filename>')
def download(filename):
	return send_from_directory('/', filename, as_attachment=True)

@app.teardown_appcontext
def shutdown_session(response_or_exc):
    if app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']:
        if response_or_exc is None:
            db.session.commit()

    db.session.remove()
    return response_or_exc

@app.route('/clear')
def clear():
    print (session.get('username'))
    # 清除session中所有数据
    session.clear()
    print (session.get('username'))
    return ('<h1>success</h1>')

@manager.command
def deploy():
	upgrade()


if __name__ == '__main__':
	manager.run()
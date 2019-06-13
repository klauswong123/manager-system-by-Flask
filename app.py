from flask import render_template, redirect, url_for, flash, abort, session, request, jsonify, send_from_directory
from setting import app, db
from models import Users, Coupon, Jewelrys
from forms import LoginForm
from flask_migrate import Migrate, MigrateCommand, upgrade
from flask_script import Manager
from credit_shop.creditshop import credit
from admin.admin import admin
from admin.admin_coupon import admin_coupon
from admin.admin_credit import admin_credit
from coupon.coupon import coupon

app.register_blueprint(credit)
app.register_blueprint(admin)
app.register_blueprint(admin_coupon)
app.register_blueprint(admin_credit)
app.register_blueprint(coupon)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get('user_id') is None:
        form = LoginForm()
        if form.validate_on_submit():
            if Users.query.filter_by(id=form.id.data).first() is None:
                flash("賬號錯誤")
                return redirect(url_for('login'))
            user = Users.query.filter_by(id=form.id.data).first()
            # 验证密码是否正确
            if user.password != form.password.data:
                flash("密码錯誤")
                return redirect(url_for('login'))
            # 记住登录状态
            session['user_id'] = user.id
            # 根据身份重定向
            return redirect('/u/' + str(user.id))
        return render_template('form.html', form=form)
    else:
        id = session.get('user_id')
        return redirect('/u/' + str(id))


@app.route('/logout')
def logout():
    if session.get('admin'):
        session['admin'] = None
    # 普通用户退出
    elif session.get('user_id') is None:
        flash("未登录")
        return redirect(url_for('login'))
    flash("退出成功")
    session['user_id'] = None
    return redirect(url_for('login'))


@app.route('/u/<string:id>')
def user(id):
    # 验证是否已登录
    if session.get('user_id') is None or id != session.get('user_id'):
        session['user_id'] = None
        flash("未登录")
        return redirect(url_for('login'))
    user = Users.query.filter_by(id=id).first()
    # 验证身份
    return render_template('user.html', user=user)

# 错误页面路由控制
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
    print(session.get('username'))
    # 清除session中所有数据
    session.clear()
    print(session.get('username'))
    return ('<h1>success</h1>')


@manager.command
def deploy():
    upgrade()


if __name__ == '__main__':
    manager.run()

from flask import Blueprint, session, render_template, flash, redirect, url_for,abort,request, jsonify
from models import Users
from forms import AdminForm,AdminAddForm,SearchForm
from setting import db,app
import os

admin = Blueprint('admin', __name__, url_prefix='/admin' ,template_folder='templates',static_folder='.static')

@admin.route('/', methods=['GET', 'POST'])
def admin_page():
    if not session.get('admin'):
        form = AdminForm()
        if form.validate_on_submit():
            session['admin'] = True
            return redirect('/admin/control')
        return render_template('form.html', form=form)
    else:
        return redirect(url_for('admin.control'))

@admin.route('/search', methods=['GET', 'POST'])
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

@admin.route('/change', methods=['POST'])
def change():
    if not session.get('admin'):
        abort(400)
    user = Users.query.filter_by(key=request.form.get('key')).first()
    user.id = request.form.get('id')
    user.password = request.form.get('password')
    user.credit = request.form.get('credit')
    db.session.add(user)
    return jsonify({'result': 'success'})

#允許檔案類型
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
basedir = os.path.abspath(os.path.dirname(__file__))

@admin.route('/control', methods=['GET', 'POST'])
def control():
    if not session.get('admin'):
        abort(400)
    users = Users.query.all()
    if request.method == 'POST':
        if request.files['file1']:
            file = request.files['file1']
            if file.filename == '':
                flash('No selected file')
                return url_for('admin.control')
            if file and allowed_file(file.filename):
                new_filename = '321.jpg'
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
                flash("上傳成功")
    return render_template('control.html', users=users, admin=True)

# 管理员新增用户路由控制
@admin.route('/add', methods=['GET', 'POST'])
def admin_add():
    if not session.get('admin'):
        abort(400)
    form = AdminAddForm()
    if form.validate_on_submit():
        user = Users(id=form.id.data, password=form.password.data)
        db.session.add(user)
        flash('增加成功')
        return redirect(url_for('admin.control'))
    return render_template('adminadd.html', form=form)

# 管理员删除用户路由控制
@admin.route('/delete', methods=['POST'])
def admin_delete():
    if session.get('admin'):
        user = Users.query.filter_by(id=request.form.get('id')).first()
        if user:
            db.session.delete(user)
        return 'ok'
    abort(400)
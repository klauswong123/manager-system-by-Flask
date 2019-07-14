'''from flask import Blueprint, session, render_template, flash, redirect, url_for,abort
from models import Jewelrys, Users, Jewelrys_Photos
from forms import Add_photo, Show_photo
from setting import db,app
import os

admin_group = Blueprint('admin_group', __name__, url_prefix='/admin/group_shop' ,template_folder='templates',static_folder='static')

@admin_group.route('/', methods=['GET', 'POST'])
def group_goods():
    if not session.get('admin'):
        abort(400)
    jewelrys = []
    jewelrys.append(Jewelrys.query.filter_by(image='group1.jpg',status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='group2.jpg',status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='group3.jpg',status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='group4.jpg',status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='group5.jpg',status=True).first())
    jewelrys.append(Jewelrys.query.filter_by(image='group6.jpg',status=True).first())
    number = []
    number.append(int(Jewelrys.query.filter_by(image='group1.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='group2.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='group3.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='group4.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='group5.jpg', status=True).count()))
    number.append(int(Jewelrys.query.filter_by(image='group6.jpg', status=True).count()))
    return render_template('admin_credit_shop.html', jewelry=jewelrys, number=number)

#添加積分商品
@admin_group.route('/add_credit/<string:file>', methods=['GET','POST'])
def add_credit(file):
    if not session.get('admin'):
        abort(400)
    form = Add_photo()
    if form.validate_on_submit():
        for jew in (Jewelrys.query.filter_by(image=file)):
            jew.status=False
            db.session.add(jew)
        filename = file
        image = form.photo.data
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        text = form.text.data
        credit = form.credit.data
        number = form.number.data
        for i in range(int(number)):
            jewelry = Jewelrys(name=text, credit=credit, image=filename)
            db.session.add(jewelry)
        return redirect(url_for('admin_credit.credit_goods'))
    return render_template('credit_form.html', form=form)

@admin_group.route('/del_credit/<string:file>', methods=['GET', 'POST'])
def del_credit(file):
    if not session.get('admin'):
        abort(400)
    for del_jew in (Jewelrys.query.filter_by(image=file)):
        if del_jew.status==True:
            db.session.delete(del_jew)
    return redirect(url_for('admin_credit.credit_goods'))

#admin查看用戶兌換情況
@admin_group.route('/goods', methods=['GET','POST'])
def admin_goods():
    if not session.get('admin'):
        abort(400)
    users = Users.query.all()
    jewelrys = []
    for user in users:
        if user.jewelry:
            for jew in user.jewelry:
                jewelrys.append(jew)
    return  render_template('admin_goods.html',jewelrys=jewelrys)

@admin_group.route('/add_photos/<string:file>', methods=['GET','POST'])
def add_group(file):
    if not session.get('admin'):
        abort(400)
    form = Add_photo()
    if form.validate_on_submit():
        for jew in (Jewelrys.query.filter_by(image=file)):
            jew.status=False
            db.session.add(jew)
        filename = file
        image = form.photo.data
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        text = form.text.data
        credit = form.credit.data
        number = form.number.data
        for i in range(int(number)):
            jewelry = Jewelrys(name=text, credit=credit, image=filename)
            db.session.add(jewelry)
        return redirect(url_for('admin_credit.credit_goods'))
    return render_template('credit_form.html', form=form)

@admin_group.route('/show_photos/<string:file>', methods=['GET','POST'])
def show_group(file):
    if not session.get('admin'):
        abort(400)
    form = Show_photo()
    if form.validate_on_submit():
        jewelry = Jewelrys.query.filter_by(image=file).first()
        photos = Jewelrys_Photos.query.filter_by(jewelry_name = jewelry.name)
        numbers = []
        for photo in photos:
            numbers.append(photo.number)
        for i in range(1,21):
            if i not in numbers:
                number = i
        filename = file + '_' + str(number)
        image = form.photo.data
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        for i in range(int(number)):
            jewelry = Jewelrys(image=filename)
            db.session.add(jewelry)
        return redirect(url_for('admin_group.show_group'))
    return render_template('admin_group.html', form=form)'''
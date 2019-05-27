@app.route('/admin/credit_shop', methods=['GET', 'POST'])
def add_goods():
    jewelrys = []
    jewelrys.append(Jewelrys.query.filter_by(image='file1.jpg').first())
    jewelrys.append(Jewelrys.query.filter_by(image='file2.jpg').first())
    jewelrys.append(Jewelrys.query.filter_by(image='file3.jpg').first())
    jewelrys.append(Jewelrys.query.filter_by(image='file4.jpg').first())
    jewelrys.append(Jewelrys.query.filter_by(image='file5.jpg').first())
    jewelrys.append(Jewelrys.query.filter_by(image='file6.jpg').first())
    if request.method == 'POST':
        if request.files['file1']:
            file = request.files['file1']
            if file.filename == '':
                flash('No selected file')
                return url_for(control)
            if file and allowed_file(file.filename):
                new_filename = 'file1.jpg'
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
                if request.values.get('name1'):
                    text = request.values.get('name1')
                    credit = request.values.get('credit1')
                    number = request.values.get('number1')
                    for i in range(int(number)):
                        jewelry = Jewelrys(name=text, credit=credit, image=new_filename)
                        db.session.add(jewelry)
                        flash("上傳成功")
                    return render_template('admin_credit_shop.html', jewelry=jewelrys)
        if request.files['file2']:
            file = request.files['file2']
            if file.filename == '':
                flash('No selected file')
                return url_for(control)
            if file and allowed_file(file.filename):
                new_filename = 'file2.jpg'
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
                if request.values.get('name2'):
                    text = request.values.get('name2')
                    credit = request.values.get('credit2')
                    number = request.values.get('number2')
                    for i in range(int(number)):
                        jewelry = Jewelrys(name=text, credit=credit, image=new_filename)
                        db.session.add(jewelry)
                        flash("上傳成功")
                    return render_template('admin_credit_shop.html', jewelry=jewelrys)
        if request.files['file3']:
            file = request.files['file3']
            if file.filename == '':
                flash('No selected file')
                return url_for(control)
            if file and allowed_file(file.filename):
                new_filename = 'file3.jpg'
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
                if request.values.get('name3'):
                    text = request.values.get('name3')
                    credit = request.values.get('credit3')
                    number = request.values.get('number3')
                    for i in range(int(number)):
                        jewelry = Jewelrys(name=text, credit=credit, image=new_filename)
                        db.session.add(jewelry)
                        flash("上傳成功")
                    return render_template('admin_credit_shop.html', jewelry=jewelrys)
        if request.files['file4']:
            file = request.files['file4']
            if file.filename == '':
                flash('No selected file')
                return url_for(control)
            if file and allowed_file(file.filename):
                new_filename = 'file4.jpg'
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
                if request.values.get('name4'):
                    text = request.values.get('name4')
                    credit = request.values.get('credit4')
                    number = request.values.get('number4')
                    for i in range(int(number)):
                        jewelry = Jewelrys(name=text, credit=credit, image=new_filename)
                        db.session.add(jewelry)
                        flash("上傳成功")
                    return render_template('admin_credit_shop.html', jewelry=jewelrys)
        if request.files['file5']:
            file = request.files['file5']
            if file.filename == '':
                flash('No selected file')
                return url_for(control)
            if file and allowed_file(file.filename):
                new_filename = 'file5.jpg'
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
                if request.values.get('name5'):
                    text = request.values.get('name5')
                    credit = request.values.get('credit5')
                    number = request.values.get('number5')
                    for i in range(int(number)):
                        jewelry = Jewelrys(name=text, credit=credit, image=new_filename)
                        db.session.add(jewelry)
                        flash("上傳成功")
                    return render_template('admin_credit_shop.html', jewelry=jewelrys)
        if request.files['file6']:
            file = request.files['file6']
            if file.filename == '':
                flash('No selected file')
                return url_for(control)
            if file and allowed_file(file.filename):
                new_filename = 'file6.jpg'
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
                if request.values.get('name6'):
                    text = request.values.get('name6')
                    credit = request.values.get('credit6')
                    number = request.values.get('number6')
                    for i in range(int(number)):
                        jewelry = Jewelrys(name=text, credit=credit, image=new_filename)
                        db.session.add(jewelry)
                        flash("上傳成功")
                    return render_template('admin_credit_shop.html', jewelry=jewelrys)
    return render_template('admin_credit_shop.html',jewelry=jewelrys)

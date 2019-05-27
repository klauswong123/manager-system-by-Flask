from flask_wtf import FlaskForm
from flask import session
from wtforms import StringField, SubmitField, PasswordField, ValidationError, IntegerField, DateTimeField, BooleanField, FileField
from wtforms.validators import Email, DataRequired, Length, EqualTo
from models import Users,Coupon


class AdminForm(FlaskForm):
    #郵箱認證
    def account_check(self,field):
        if field.data != 'klauswangjinpeng@gmail.com':
            raise ValidationError('賬號錯誤')
    def password_check(self,field):
        if field.data != '1314wang.':
            raise ValidationError('密碼錯誤')
    email = StringField("管理者郵箱",validators=[DataRequired(message='郵箱是空的'),
                                            Email(message=u'不是郵箱'),account_check])
    password = PasswordField("管理者密碼",validators=[DataRequired(message='密碼錯誤'),password_check])
    login = SubmitField("管理者登陸")


class LoginForm(FlaskForm):
    def id_exist(self, field):
        if not  Users.query.filter_by(id=field.data).first():
            raise ValidationError('此ig賬號不存在')
    id = StringField('ig賬號', validators=[DataRequired(message='請輸入ig賬號')])
    password = PasswordField('密碼',validators=[DataRequired(message='輸入密碼')])
    login = SubmitField("登入")

class Add_photo(FlaskForm):
    photo = FileField(validators=[DataRequired()])
    text = StringField('積分商品説明', validators=[DataRequired(message='請輸入積分商品内容')])
    credit = StringField('所需積分', validators=[DataRequired(message='請輸入所需積分')])
    number = StringField('生成數量', validators=[DataRequired(message='請輸入生成數量')])
    submit = SubmitField("添加積分商品")


class AdminAddForm(FlaskForm):
    def password_noblank(self,field):
        for s in field.data:
            if s == ' ':
                raise ValidationError('密碼中不能有空格')

    def id_unique(self, field):
        if Users.query.filter_by(id=field.data).first():
            raise ValidationError('id存在')

    id = StringField('ig_id', validators=[DataRequired(message='請輸入ig賬號'), id_unique])
    password = PasswordField('密碼', validators=[DataRequired(message='請輸入密碼'), password_noblank])
    add = SubmitField("增加用户")

class Coupon_CreateForm(FlaskForm):
    number = IntegerField('輸入生成數量',validators=[DataRequired(message='請輸入')])
    submit = SubmitField("生成新的優惠券")

class Coupon_TakeForm(FlaskForm):
    phone = StringField('請輸入手機後四位號碼',validators=[DataRequired(message='請輸入手機後四位號號'), Length(min=4,max=4)])
    submit = SubmitField('領取優惠劵')

class SearchForm(FlaskForm):
	keyword = StringField("输入查询关键字", validators=[DataRequired(message="输入不能为空")])
	search = SubmitField("Find It!")



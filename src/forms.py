import flask_wtf
import wtforms
from wtforms import validators

'''
预定课程  输入预定信息 校验
'''
class ScheduleForm(flask_wtf.Form):
    childname = wtforms.StringField('小朋友姓名',validators=[validators.input_required(message=u'小朋友姓名不能为空')])
    phone     = wtforms.StringField('家长手机号',validators=[validators.regexp(r'1\d{10}$', message=u'请输入正确的手机号')])  #对手机号进行校验
    childage  = wtforms.StringField('小朋友年龄',validators=[validators.regexp(r'\d{1,2}$', message=u'请正确输入小朋友年龄')])
    # date = wtforms.StringField('日期',validators=[validators.input_required(message="请输入预约日期")])

'''
登陆注册 校验
'''

class AuthForm(flask_wtf.FlaskForm):
    # 手机号
    phone = wtforms.StringField('手机号', validators=[validators.regexp(r'1\d{10}$', message=u'请输入正确的手机号')])
    # 登录密码
    passwd = wtforms.PasswordField('密码', validators=[validators.DataRequired(u'密码不能为空')])


class SignupForm(AuthForm):
    # 用户名
    username = wtforms.StringField('用户名', validators=[validators.DataRequired(u'用户名不能为空')])

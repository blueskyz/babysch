import wtforms
from wtforms import validators

'''
预定课程  输入预定信息 校验
'''
class ScheduleForm(wtforms.Form):
    phone = wtforms.StringField(validators=[validators.length(min=11,max=11)])  #对手机号进行校验
    date = wtforms.StringField(validators=[validators.input_required()])

'''
登陆注册 校验
'''
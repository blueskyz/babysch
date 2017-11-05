#!/usr/bin/env python
# coding: utf-8


from flask import render_template, flash, request, redirect
from . import auth
from forms import AuthForm, SignupForm
from login import User, login_manager
from flask_login import login_user, logout_user, login_required
from models import UserModel
from exts import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = AuthForm()

    # 验证手机号密码
    if form.validate_on_submit():
        phone = request.form.get('phone')
        passwd = request.form.get('passwd')
        user_info = User.query.filter_by(telephone=phone).first()
        if user_info and user_info.check_password(passwd):
            login_user(user_info)
            return redirect('/')
        else:
            flash('用户名密码不匹配')

    return render_template('auth/login.html', form=form)


# @auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    # 验证手机号是否被注册过
    if form.validate_on_submit():
        phone = request.form.get('phone')
        username = request.form.get('username')
        passwd = request.form.get('passwd')

        user_info = UserModel.query.filter_by(telephone=phone).first()
        if user_info:
            flash('该手机号已被注册')
            return render_template('auth/signup.html', form=form)

        user = UserModel(username=username, telephone=phone, password=passwd)
        db.session.add(user)
        db.session.commit()

        # 注册成功, 登录
        return redirect('/login')

    return render_template('auth/signup.html', form=form)


@auth.route('/logined', methods=['GET'])
@login_required
def test_authed():
    return 'logined'

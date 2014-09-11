# coding: utf-8

from flask import g
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from ..blueprint import bp  # noqa
from ..forms.login import LoginForm
from ..src import WrongCredentials
from ..src import get_user
from ..src import log_user_in
from ..src import log_user_out

@bp.route('/login/')
def login():

    next = request.args.get('next')
    form = LoginForm(next=next)
    return render_template('login.html',
        form=form,
        next=next)

@bp.route('/login/', methods=['POST'])
def login_post():

    form = LoginForm(request.formdata)
    if form.validate():
        next = form.next.data
        email = form.email.data
        password = form.password.data

        try:
            user = get_user(email, password)
            log_user_in(user)
            return redirect(next)
        except WrongCredentials:
            form.password.errors.append(u"Error")
            log_user_out()

    return render_template('login.html',
        form=form)

@bp.route('/logout/')
def logout():

    log_user_out()
    return redirect(url_for('user.login'))
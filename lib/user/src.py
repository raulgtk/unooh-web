# coding: utf-8

from functools import wraps

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from flask import g
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from .models.user import User

class WrongCredentials(Exception):
    pass

def get_user_by_session(session_id):
    try:
        user = User.get(session_id=session_id)
    except (NoResultFound, MultipleResultsFound):
        raise WrongCredentials
    return user

def get_user(email, password):
    try:
        user = User.get(email=email)
    except (NoResultFound, MultipleResultsFound):
        raise WrongCredentials("Wrong user")

    # check pass
    pass_ok = user.check_password(password)
    if not pass_ok:
        raise WrongCredentials("Wrong password")

    return user

def log_user_in(user):
    session['session_id'] = user.session_id
    session.modified = True

def log_user_out():
    if 'session_id' in session:
        del(session['session_id'])
        session.modified = True

def login_required(controller):
    @wraps(controller)
    def decorated_controller(*args, **kargs):
        if not g.user.is_authenticated():
            return redirect(url_for('user.login', next=request.url))
        return controller(*args, **kargs)
    return decorated_controller
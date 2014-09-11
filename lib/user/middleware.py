# coding: utf-8

from flask import g
from flask import session

from init import app
from .models.user import AnonymousUser  # noqa
from .src import get_user_by_session
from .src import WrongCredentials

@app.before_request
def get_current_user():

    # get session id
    if 'session_id' not in session or not session['session_id']:
        g.user = AnonymousUser()
        return

    # check if user is valid
    try:
        g.user = get_user_by_session(session['session_id'])
    except WrongCredentials:
        g.user = AnonymousUser()


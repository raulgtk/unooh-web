# coding: utf-8

from init import app

from .models.db import session  # noqa

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()
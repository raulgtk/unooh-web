# coding: utf-8

from flask import g
from flask import render_template

from ..blueprint import bp

@bp.route('/')
def test():
    title = u"Test page"
    return render_template('layout/base.html',
        title=title)
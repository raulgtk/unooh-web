# coding: utf-8

from flask import g
from flask import render_template

from ..blueprint import bp

@bp.route('/')
def home():
    title = u"unooh"
    return render_template('layout/base.html',
        title=title)
# coding: utf-8

import json

from flask import g
from flask import render_template
from lib.cors import crossdomain

from ..blueprint import bp

@bp.route('/')
def home():
    title = u"unooh"
    return render_template('layout/base.html',
        title=title)

@bp.route('/api_test/menu', methods=['POST', 'OPTIONS', 'GET'])
@crossdomain(origin='*', headers=['Content-Type'])
def api_menu():
    data = []
    data.append({ 'id': 'NO01', 'name': u"Novedades" })
    data.append({ 'id': 'BO03', 'name': u"Temáticos" })
    data.append({ 'id': 'AC12', 'name': u"Actualidad" })
    data.append({ 'id': 'DI01', 'name': u"Diseño" })
    data.append({ 'id': 'AG02', 'name': u"Agenda" })
    return json.dumps({'data':data})
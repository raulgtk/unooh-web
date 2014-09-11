# conding: utf-8

from flask import Blueprint

bp = Blueprint('layout', __name__, template_folder='templates', static_folder='static')
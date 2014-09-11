# coding: utf-8

import os
import importlib

def setup_lib(app):
    packages = app.config['LIB']
    for package in packages:
        module = importlib.import_module('lib.%s' % package)
        app.register_blueprint(module.bp)

def setup_web(app):
    packages = app.config['WEB']
    for package in packages:
        module = importlib.import_module('web.%s' % package)
        app.register_blueprint(module.bp)

def setup_adm(app):
    packages = app.config['ADM']
    for package in packages:
        module = importlib.import_module('adm.%s' % package)
        app.register_blueprint(module.bp)
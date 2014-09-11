# coding: utf-8

import os

from flask import abort
from flask import render_template
from flask import send_from_directory

from .application import app
from .application import manager_static

if app.debug:
    @app.route('/static/<path:filename>')
    def static(filename=None):
        manager_static.collect(verbose=False)
        static_root = app.config['STATIC_ROOT']
        asset_path = os.path.join(app.project_dir, static_root, filename)
        asset_dir = os.path.dirname(asset_path)
        asset_filename = os.path.basename(asset_path)
        return send_from_directory(asset_dir, asset_filename)

    @app.route('/media/<path:filename>')
    def media(filename=None):
        media_root = app.config['MEDIA_ROOT']
        asset_path = os.path.join(app.project_dir, media_root, filename)
        asset_dir = os.path.dirname(asset_path)
        asset_filename = os.path.basename(asset_path)
        return send_from_directory(asset_dir, asset_filename)


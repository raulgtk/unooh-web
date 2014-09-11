# coding: utf-8

import os

from .application import app

def static(filename):
    return app.config['STATIC_URL'] + filename

def media(filename):
    return app.config['MEDIA_URL'] + filename

@app.context_processor
def context_processor():
    return {
        'static': static,
        'media': media,
    }
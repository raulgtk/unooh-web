# coding: utf-8

import os

from init import app
from .src import get_thumb

@app.template_filter('thumb')
def thumb(filename, size='100x0', directory='images'):
    if not filename:
        return None
    return get_thumb(filename, size, directory)

@app.template_filter('part')
def part(filename, size='100x0', directory='parts'):
    if not filename:
        return None
    return get_thumb(filename, size, directory)

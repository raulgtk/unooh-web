# coding: utf-8

from flask import request

from .application import app

@app.before_request
def add_formdata_attr():

    # add request files to formdata
    if request.files:
        formdata = request.form.copy()
        formdata.update(request.files)
    else:
        formdata = request.form

    request.formdata = formdata
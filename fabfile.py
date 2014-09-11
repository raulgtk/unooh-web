# coding: utf-8

import IPython

from fabric.api import task
from fabric.api import local
from fabric.api import settings
from fabric.utils import abort
from fabric.operations import prompt
from fabric.contrib.console import confirm

from init import app
from init import manager_static
from lib.dbtools import create_all
from lib.dbtools import drop_all
from bin.db_sample import insert_sample_data

@task
def run(host=None):
    """ Run development server """
    if host:
        app.host = host
    app.run()

@task
def shell():
    """ Run debug shell """
    IPython.embed()

@task
def collect_static(host=None):
    """ Collect static """
    manager_static.collect(verbose=True)

@task
def db_devel():
    """ Reset database and insert sample data """
    if not app.debug:
        abort("Database cannot be reset when in production mode (ie. DEBUG = False)")

    print "The database contents will be deleted."
    if confirm("Are you sure?"):
        print "Inserting sample data..."
        drop_all(app.config['DB_URI'])
        create_all()
        insert_sample_data()
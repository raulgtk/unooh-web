# coding: utf-8

from .application import app
from .application import manager_static
from .src import setup_lib
from .src import setup_web
from .src import setup_adm

import middleware
import context
import system

setup_lib(app)
setup_web(app)
setup_adm(app)
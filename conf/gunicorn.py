import os
from init import app

proc_name = 'unooh'
bind = 'unix:/tmp/gu_%s.sock' % proc_name
workers = 3
pythonpath = app.project_dir
accesslog = None
errorlog = os.path.join(app.project_dir, 'log/gunicorn.log')
loglevel = 'error'
user = 'code'
preload_app = True
max_requests = 1000
worker_class = 'sync'
threads = 1
timeout = 220
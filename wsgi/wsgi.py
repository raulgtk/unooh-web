import os
import sys
from werkzeug.contrib.fixers import ProxyFix
# allow errors and print statements be redirected to error.log
sys.stdout = sys.stderr

# get project dir
project_path = os.getcwd()

## activate virtualenv
#activate_this = os.path.join(project_path, 'venv/bin/activate_this.py')
#execfile(activate_this, dict(__file__=activate_this))

# retrieve app
from init import app as application

# enable debugging mode if necessary
if application.debug:

    # start interactive debugger
    from werkzeug.debug import DebuggedApplication
    application = DebuggedApplication(application, evalex=True)

else:
    # add this fix when working behind a proxy
    application.wsgi_app = ProxyFix(application.wsgi_app)


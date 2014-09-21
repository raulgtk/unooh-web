#!/bin/bash

NAME="unooh"
FLASKDIR="/home/code/deploy/unooh/"
VIRTUALENV="/home/code/deploy/unooh/venv/"
SOCKFILE="/tmp/gu_unooh.sock"
ERRORLOG="/home/code/deploy/ekalaiki/log/gu_error.log"
USER="code"
GROUP="code"
NUM_WORKERS=3
WSGI_MODULE="wsgi.wsgi"

echo "Starting $NAME as $USER"

# Activate the virtual environment
source $VIRTUALENV/bin/activate
cd $FLASKDIR
export PYTHONPATH=$FLASKDIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec gunicorn ${WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --log-level=error \
    --bind=unix:$SOCKFILE \
    --error-logfile=$ERRORLOG \
    --max-requests 500
    --preload


#!/bin/sh

/home/mo/.local/bin/gunicorn --bind 0.0.0.0:32841 autoapp:app

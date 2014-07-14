#!/bin/sh
uwsgi --http :9090 --wsgi-file app_uwsgi.py --master --processes 1 --threads 2
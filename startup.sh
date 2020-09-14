#!/bin/sh

python manage.py migrate --database=auth_db

while :; do
    python manage.py runserver 0.0.0.0:8001
    sleep 1
done
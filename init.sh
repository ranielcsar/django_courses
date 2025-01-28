#!/bin/bash
source /app/ambient/bin/activate
python /app/courses/manage.py runserver 0.0.0.0:8000

#!/bin/bash -x


DJANGO_SETTINGS_MODULE=config.settings.prod python3 manage.py migrate --noinput || exit 1
#
DJANGO_SETTINGS_MODULE=config.settings.prod python3 manage.py collectstatic --noinput || exit 1


DJANGO_SETTINGS_MODULE=config.settings.prod python3 manage.py runserver 0.0.0.0:8002 || exit 1

DJANGO_SETTINGS_MODULE=config.settings.prod python3 manage.py start_kafka_consumer || exit 1


wait
exec "$@"

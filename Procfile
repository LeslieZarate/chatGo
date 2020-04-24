web: daphne settings.asgi:application --port $PORT --bind 0.0.0.0 -v2 --preload
worker: python settings/manage.py runworker -v2
# GeneratingHTML

pip install falcon
pip install gunicorn

gunicorn -D --error-logfile /tmp/gunicorn_error.log index:app

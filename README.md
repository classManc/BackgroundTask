
# BackgroundTask

A Django project that uses celery to perform asynchronous task periodically when a view is called



## How to run:

open the the terminal and activate virtual environment using the command: "source env/bin/activate"

open another erminal and start the celery worker using the command : "celery -A your_project_name worker --loglevel=info -B"

open another terminal to connect to the redis server using the command: "redis-server"

in the terminal you opened the virtual environment, run python3 manage.py runserver


## required packages

pip3 install redis

pip3 install celery

brew install redis

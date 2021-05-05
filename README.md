# Swagger Execute Issue

Code demonstrating issue with running Execute on swagger with drf-spectacular.

## Run with Docker

Use commands below to run with docker-compose:

```
docker-compose up
```

The navigate to: [http://127.0.0.1:8001](http://127.0.0.1:8000)


## With without Docker

To run without Docker, use the commands below:

```shell
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python app/manage.py migrate
python app/manage.py runserver 0.0.0.0:8001
```

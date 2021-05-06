# hello-flask

This is a simple tutorial on how to create your first flask web app based on [the flask Quick start tutorial](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

## Some definitions

[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a micro-framework that enables one to create websites without enforcing so many of the design decisions. It comes with the basic modules to create a website including a development server, templating engine (Jinja2).

It has a good ecosystem with packackages that handle other things like an ORM [Sqlalchemy-Flask](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) to access the database, authentication packages etc.

## How to run

- Make sure the environment is activated
- Add the environment variable to set the name of the module

  ```bash
  export FLASK_APP=app.py
  ```

- Run the flask app

  ```bash
  flask run
  ```

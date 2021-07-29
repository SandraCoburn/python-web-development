# python-web-development

Web Development with Python - Practice

## Teck Stack

- HTML
- Python
- [Flask](https://flask.palletsprojects.com/en/2.0.x/api/) is a lightweight WSGI web application framework. It is <strong>designed to make getting started quick and easy, with the ability to scale up to complex applications.</strong> It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
- [venv](https://docs.python.org/3/library/venv.html) -> Creation of virtual environments

### Most Used CL commands

- python3 -m venv #Creates a new virtual environmente
- . venv/bin/activate
- pip install Flask

#### Minimal Flask application:

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Command Line:

```
$ export FLASK_APP=server.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

To turn the debug mode on:

```
export FLASK_ENV=development
```

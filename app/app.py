from time import sleep

from flask import Flask

WECOME_TEXT="Hello variable check k8s deployment!"

def create_app() -> Flask:
    """ create basic flask app"""
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/')
def index():
    """ index route """
    return "Hello variable check k8s deployment!"


@app.route('/timeout')
def timeout_request():
    """ route to test timeout """
    sleep(35)
    return ""

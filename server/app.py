#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)  #refers to the name of the current module app.py

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

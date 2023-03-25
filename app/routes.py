from app import exm
from flask import render_template

@emx.route('/')
def index():
    return "Hello"
from app import exm
from flask import render_template

@exm.route('/')
def index():
    return "Hello"

from flask import render_template
from . import main

@main.route('/')
def hello_world():
	return 'hello world!'


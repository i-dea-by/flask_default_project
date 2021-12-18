from flask import render_template
from . import example


@example.route('/')
def index():
    return render_template('index.html', title='default index page')

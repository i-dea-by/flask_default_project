from flask import Blueprint, render_template

# Blueprint Configuration
module = Blueprint(
    'example_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@module.route('/')
def index():
    return render_template('index.html', title='default index page')

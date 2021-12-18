from flask import Blueprint

# Blueprint Configuration
example = Blueprint('example', __name__, template_folder='templates', static_folder='static')

from . import routes, models

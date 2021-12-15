from flask import render_template, Blueprint

# Blueprint Configuration
module = Blueprint(
    'admin_bp', __name__
    # template_folder='templates',
    # static_folder='static'
)

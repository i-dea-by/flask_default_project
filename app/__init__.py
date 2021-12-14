from flask import Flask

from .db import db


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    # db.init_app(app)

    if app.debug:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass

    with app.app_context():
        # Include our Routes
        import app.main.routes as main

        # Register Blueprints
        app.register_blueprint(main.module)

        return app

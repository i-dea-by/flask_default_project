from flask import Flask
from flask_admin import Admin, AdminIndexView

from .db import db, migrate

admin = Admin()


def init_app():
    """ Инициализация ядра приложения """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # инициализация БД и миграций
    db.init_app(app)
    migrate.init_app(app, db)

    # admin = Admin(app)
    admin.init_app(app, index_view=AdminIndexView(url=app.config['ADMIN_URL']))

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

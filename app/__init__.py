import os

from flask import Flask
from flask_admin import Admin, AdminIndexView

from .db import db, migrate

admin = Admin()


def create_app():
    # загрузка из окружения режима работы flask (Prod или Dev)
    app_mode = os.getenv("APP_SETTINGS", "config.ProductionConfig")
    # инициализация ядра приложения
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_mode)
    # инициализация БД и миграций
    db.init_app(app)
    migrate.init_app(app, db)
    # инициализация админки
    admin.init_app(app, index_view=AdminIndexView(url=app.config['ADMIN_URL']))

    if app.debug:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass

    with app.app_context():
        """ регистрация приложений: routes & blueprints """
        # admin blueprint
        import app.admin.routes as admin_bp
        app.register_blueprint(admin_bp.module)
        # example blueprint
        import app.example.routes as example_bp
        app.register_blueprint(example_bp.module)

        return app

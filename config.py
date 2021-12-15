from os import environ, path

from dotenv import load_dotenv

dotenv_path = path.join(path.dirname(__file__), '.env')
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    raise FileNotFoundError('Создайте и заполните .env файл в корне проекта!')


class Config:
    """ Базовая конфигурация """
    DEBUG = False
    SECRET_KEY = environ['SECRET_KEY']
    # Включение защиты против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = True
    # URI используемая для подключения к базе данных
    SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

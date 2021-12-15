from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


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

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.163.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT','587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS','true').lower() in ['true','on','1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    FLASK_MAIL_SUBJECT_PREFIX = '[FLASKY]'
    FLASK_MAIL_SENDER = 'Flasky Admin<flasky@example.com>'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql://pyuser:123456@localhost/flaskdev'

class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('Test_DATABASE_URL') or 'mysql://pyuser:123456@localhost/flasktest'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql://pyuser:123456@localhost/flaskprod'

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}



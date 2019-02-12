import os
from peewee import SqliteDatabase, PostgresqlDatabase
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = False
    DATABASE = {
        'name': 'test.db',
        'engine': 'peewee.SqliteDatabase'
    }

class TestingConfig(Config):
    TESTING = True
    pass


class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

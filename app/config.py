import os
from peewee import SqliteDatabase, PostgresqlDatabase
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # DATABASE = {
    #     'name': 'test.db',
    #     'engine': 'peewee.SqliteDatabase'
    # }
    # project_folder = os.getcwd()
    DATABASE = SqliteDatabase('test.db')



class TestingConfig(Config):
    TESTING = True
    pass


class ProductionConfig(Config):
    DATABASE = SqliteDatabase('test.db')
    DEBUG = False



config_select = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

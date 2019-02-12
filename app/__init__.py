from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from test_app.config import config

#db modules
from flask_peewee.db import Database
#db migratiom
from peewee_moves import DatabaseManager


bootstrap = Bootstrap()
moment = Moment()
db = Database()  #Using to configure db in run-tine and initialize with delay
#db_manager = DatabaseManager(Config.DATABASE)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)




    from .main import main_bp as main_blueprint

    app.register_blueprint(main_blueprint)



    return app


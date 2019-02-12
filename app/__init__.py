from flask import Flask
from flask_bootstrap import Bootstrap

from app.config import config_select

#db modules
from flask_peewee.db import Proxy
db = Proxy()  #Using to configure db in run-tine and initialize with delay


#visual
bootstrap = Bootstrap()

def create_app(config_name="None"):
    app = Flask(__name__)

    if config_name == None:
        config_name = 'default'

    app.config.from_object(config_select[config_name])
    db.initialize(config_select[config_name].DATABASE)  # initialize a real db via proxy

    bootstrap.init_app(app)


    from app.blueprints.main import main_bp as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.blueprints.kifa import kifa_bp
    app.register_blueprint(kifa_bp)

    from app.blueprints.kuhhar import kuhhar_bp
    app.register_blueprint(kuhhar_bp)





    return app


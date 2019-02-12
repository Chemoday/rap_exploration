#!/usr/bin/env python
import os
from app import create_app
from flask_script import Manager, Shell


manager = Manager(create_app)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def generate_db():
    from app import db
    from app.config import DevelopmentConfig
    db.initialize(DevelopmentConfig.DATABASE)
    from app.database.models import MODELS_LIST
    db.create_tables(MODELS_LIST, safe=True)
    print("Db tables created")

manager.add_option('-c', '--config', dest='config_name', required=False)


if __name__ == '__main__':
    manager.run()

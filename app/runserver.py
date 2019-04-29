
#This file for PRODUCTION server start with Gunicorn
#If you develop locally - try manage.py

#Define Python project in PYTHONPATH
import sys
from os.path import dirname, abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.append(PROJECT_DIR)

#Initial project
from app import create_app
from werkzeug.contrib.fixers import ProxyFix

app = create_app(config_name='production')
app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5776)
    #host- 0.0.0.0 makes server externaly visible
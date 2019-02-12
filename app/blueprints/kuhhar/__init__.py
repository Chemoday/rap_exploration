from flask import Blueprint

analytics = Blueprint('kuhhar', __name__, url_prefix='/kuhhar')

from . import views
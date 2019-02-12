from flask import Blueprint

analytics = Blueprint('kifa', __name__, url_prefix='/kifa')

from . import views
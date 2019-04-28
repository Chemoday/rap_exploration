from flask import Blueprint

kifa_bp = Blueprint('kifa', __name__, url_prefix='/kifa')

from . import views
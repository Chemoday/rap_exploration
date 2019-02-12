from flask import Blueprint

kuhhar_bp = Blueprint('kuhhar', __name__, url_prefix='/kuhhar')

from . import views
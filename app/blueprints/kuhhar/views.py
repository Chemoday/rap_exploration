from flask import render_template, session, redirect, url_for, current_app
from . import kuhhar_bp

@kuhhar_bp.route('/', methods=['GET'])
def index():

    return render_template('kuhhar/index.html')

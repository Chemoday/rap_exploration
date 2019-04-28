from flask import render_template, session, redirect, url_for, current_app, request

from . import kifa_bp
from .forms import AssesmentForm

from app.database.models import *

@kifa_bp.route('/square_assessment', methods=['GET', 'POST'])
def square_assessment():
    form = AssesmentForm()
    query = Assessment.select().where(Assessment.rated == False).order_by(fn.Random())
    random_assessment = query.get()
    random_assessment.square_text = random_assessment.square_text.split('\n')

    return render_template('kifa/square_assessment.html',
                           random_assessment=random_assessment,
                           form=form)

@kifa_bp.route('/rate_square/<assessment_id>/', methods=['POST'])
def rate_square(assessment_id):

    if request.method == 'POST':
        q = Assessment.update({Assessment.label_0: int(request.form['label_0']),
                               Assessment.label_1: int(request.form['label_1']),
                               Assessment.label_2: int(request.form['label_2']),
                               Assessment.label_3: int(request.form['label_3']),
                               Assessment.label_4: int(request.form['label_4']),
                               Assessment.label_5: int(request.form['label_5'])}).where(Assessment.id==assessment_id)
        q.execute()
        return redirect(url_for('.square_assessment'))

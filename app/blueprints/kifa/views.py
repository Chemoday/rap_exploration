from flask import render_template, session, redirect,\
    url_for, current_app, request, flash

from . import kifa_bp
from .forms import AssesmentForm

from app.database.models import *

@kifa_bp.route('/square_assessment', methods=['GET', 'POST'])
def assessment_random_square():
    form = AssesmentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            rate_square(assessment_id=request.args.get('assessment_id'))
        else:
            flash('mark the fields')
            return redirect(url_for('.assessment_random_square'))

    query = Assessment.select().where(Assessment.rated == False).order_by(fn.Random())
    random_assessment = query.get()
    random_assessment.square_text = random_assessment.square_text.split('\n')

    return render_template('kifa/square_assessment.html',
                           random_assessment=random_assessment,
                           form=form)

def rate_square(assessment_id):
    print('Rating id: ', assessment_id)
    q = Assessment.update({Assessment.label_0: int(request.form['label_0']),
                           Assessment.label_1: int(request.form['label_1']),
                           Assessment.label_2: int(request.form['label_2']),
                           Assessment.label_3: int(request.form['label_3']),
                           Assessment.label_4: int(request.form['label_4']),
                           Assessment.label_5: int(request.form['label_5'])}).where(Assessment.id==assessment_id)
    q.execute()
    return redirect(url_for('.assessment_random_square'))

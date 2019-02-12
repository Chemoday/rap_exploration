from flask import render_template, session, redirect, url_for, current_app
from .. import db

from . import main_bp
from .forms import NameForm

from ..models import User


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        try:
            User.get(User.username == form.name.data)
            session['known'] = True
        except User.DoesNotExist:
            User.create(username=form.name.data)
            session['known'] = False

        session['name'] = form.name.data
        return redirect(url_for('main.index'))


    return render_template('index.html', form=form,
                           name=session.get('name'),
                           known=session.get('known', False))
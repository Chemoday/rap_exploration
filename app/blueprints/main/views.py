from flask import render_template, session, redirect, url_for, current_app

from . import main_bp
from .forms import NameForm

from app.database.models import *


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        if User.select(User.username == form.name.data).exists():
            User.get(User.username == form.name.data)
            session['known'] = True
        else:
            User.create(username=form.name.data)


        session['name'] = form.name.data
        return redirect(url_for('main.index'))


    return render_template('index.html', form=form,
                           name=session.get('name'),
                           known=session.get('known', False))
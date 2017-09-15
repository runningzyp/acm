from flask import render_template, session, redirect, url_for, current_app, request
from flask import flash
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    flash('hello')
    usern = form['username']
    

    return render_template('index.html')

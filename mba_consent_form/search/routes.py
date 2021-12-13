from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login.utils import login_required
from mba_consent_form.forms import SearchCustomerForm
from mba_consent_form.models import db, Customer, User
from mba_consent_form.helpers import token_required
from mba_consent_form.secrets import con

cursor = con.cursor()

searcher = Blueprint('searcher',__name__, template_folder='searcher_templates')

@searcher.route('/search', methods = ['GET', 'POST'])
@login_required
def search(current_user_token = '93851cddd1fd0856ca14c99b34161f7fcec78775'):
    form = SearchCustomerForm()
    if request.method == 'GET' and form.validate_on_submit():
        cursor.execute("select * from public.customer")
        result = cursor.fetchall()
    else:
        result = ''
    # try:
    #     if request.method == 'GET' and form.validate_on_submit():

    return render_template('search.html', form = form, data = result) # result to go in render template
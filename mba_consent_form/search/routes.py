from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login.utils import login_required
from mba_consent_form.forms import SearchCustomerForm
from mba_consent_form.models import db, Customer, User
from mba_consent_form.secrets import con

cursor = con.cursor()

searcher = Blueprint('searcher',__name__, template_folder='searcher_templates')

@searcher.route('/search', methods = ['GET', 'POST'])
@login_required
def search():
    form = SearchCustomerForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            fn = form.first_name.data
            ln = form.last_name.data
            
            cursor.execute(f"select * from public.customer where first_name = '{fn}' and last_name = '{ln}'")

            result = cursor.fetchone()
            print(result)

        else:
            fn = form.first_name.data
            ln = form.last_name.data
            result = ''
            flash('Nobody by that name(case-sensitive) category="message"')

    except:
        raise Exception('Invalid Form Data: Please check your form.')


    return render_template('search.html', form = form, result = result)
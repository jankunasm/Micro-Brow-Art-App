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
            
            # cursor.execute(f'select * from public.customer where first_name = "{fn}" and last_name = "{ln}"')
            # result = cursor.fetchone().first()
            
            search = f"select * from public.customer where first_name = '{fn}' and last_name = '{ln}'"
            cursor.execute(f"select * from public.customer where first_name = '{fn}' and last_name = '{ln}'")

            result = cursor.fetchone() # maybe .first()
            print(result)

        else:
            fn = form.first_name.data
            ln = form.last_name.data
            result = ''

            # psql_query = "select * from customer"
            # cursor.execute(psql_query)

            # customer_records = cursor.fetchone()
            # print("Print first record", customer_records)

            # customer_records2 = cursor.fetchone()
            # print("Printing second record", customer_records2)

    except:
        raise Exception('Invalid Form Data: Please check your form.')


    return render_template('search.html', form = form, result = result)
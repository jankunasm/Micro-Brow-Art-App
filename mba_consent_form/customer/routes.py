from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login.utils import login_required
from flask_migrate import current
from mba_consent_form.forms import CreateCustomerForm
from mba_consent_form.models import db, Customer
from ..authentication.routes import User
from flask_login import current_user

cust = Blueprint('cust',__name__, template_folder='customer_templates')

@cust.route('/customer', methods = ['GET', 'POST'])
@login_required
def create_customer():
    form = CreateCustomerForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            needle = form.needle.data
            machine = form.machine.data
            pigment = form.pigment.data
            brow_type = form.brow_type.data
            user_token = current_user.token
            print(first_name, last_name, needle, machine, pigment, brow_type)

            customer = Customer(first_name, last_name, needle, machine, pigment, brow_type, user_token)
            db.session.add(customer)
            db.session.commit()

            flash(f'You have successfully added {first_name} {last_name} to your database.', 'user-created')

            return redirect(url_for('site.home'))

    except:
        raise Exception('Invalid Form Data: Please check your form.')

    return render_template('customer.html', form = form)
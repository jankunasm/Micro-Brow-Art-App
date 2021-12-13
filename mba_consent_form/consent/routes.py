from flask import Blueprint, render_template
from flask_login.utils import login_required
from mba_consent_form.forms import ConsentForm

cons = Blueprint('cons',__name__, template_folder='consent_templates')

@cons.route('/consent')
@login_required
def consent():
    form = ConsentForm()

    return render_template('consent.html', form = form)
from flask import Blueprint, render_template
from flask_login.utils import login_required

cons = Blueprint('consent',__name__, template_folder='consent_templates')

@cons.route('/consent')
def consent():
    return render_template('consent.html')
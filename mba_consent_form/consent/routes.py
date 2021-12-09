from flask import Blueprint, render_template

cons = Blueprint('consent',__name__, template_folder='consent_templates')

@cons.route('/consent')
def consent():
    return render_template('consent.html')
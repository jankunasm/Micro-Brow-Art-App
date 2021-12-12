from flask import Blueprint, render_template
from flask_login.utils import login_required

searcher = Blueprint('searcher',__name__, template_folder='searcher_templates')

@searcher.route('/search')
def search():
    return render_template('search.html')
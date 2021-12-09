from flask import Blueprint, render_template

searcher = Blueprint('searcher',__name__, template_folder='searcher_templates')

@searcher.route('/search')
def search():
    return render_template('search.html')
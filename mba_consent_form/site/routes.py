from flask import Blueprint, render_template
import requests
import json

"""
    Note that in  the below code,
    some arguments are specified when creating
    BLueprint objects.  The first argument,
    'site' is the Blueprints name,
    which flask uses for routing.

    The second argument, __name__, is the Blueprint's
    import name, which flask uses to locate the 
    Blueprint's resources.
"""

site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/', methods = ['GET'])
def home():
    request = requests.get('https://zenquotes.io/api/today/49c919cd0ade1f8aa3e55ce20dc60d7053d98551')
    data = json.loads(request.content)
    print(data)
    return render_template('index.html', data = data)
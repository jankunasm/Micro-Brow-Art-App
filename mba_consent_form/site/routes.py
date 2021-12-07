from flask import Blueprint, render_template

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

@site.route('/')
def home():
    return render_template('index.html')
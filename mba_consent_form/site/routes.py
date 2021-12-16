from flask import Blueprint, render_template
import requests
import json
from mba_consent_form.secrets import apikey

site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/', methods = ['GET'])
def home():
    request = requests.get(apikey)
    data = json.loads(request.content)
    return render_template('index.html', data = data)
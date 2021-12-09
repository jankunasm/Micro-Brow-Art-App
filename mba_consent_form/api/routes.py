from flask import Blueprint

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return { 'some': "value"}



# All of this is likey useless considering the type of
# API im using .....
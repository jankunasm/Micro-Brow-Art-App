from flask import Blueprint, json, request, jsonify
from mba_consent_form.helpers import token_required
from mba_consent_form.models import db, User, Customer, customer_schema, customers_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return { 'some': "value",
            'other': 'Data'}

# Customer Creation Route
@api.route('/customers', methods = ['POST'])
@token_required
def create_customer(current_user_token):
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    needle = request.json['needle']
    machine = request.json['machine']
    pigment = request.json['pigment']
    brow_type = request.json['brow_type']
    user_token = current_user_token.token

    customer = Customer(first_name, last_name, needle, machine, pigment, brow_type, user_token)
    db.session.add(customer)
    db.session.commit()

    response = customer_schema.dump(customer)
    return jsonify(response)

# Retrieve all Customers
@api.route('/customers', methods = ['GET'])
@token_required
def get_customers(current_user_token):
    owner = current_user_token.token
    customers = Customer.query.filter_by(user_token = owner).all()
    response = customers_schema.dump(customers)
    return jsonify(response)

# Retrieve single Customer
@api.route('/customers/<id>', methods = ['GET'])
@token_required
def get_customer(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        customer = Customer.query.get(id)
        response = customer_schema.dump(customer)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Token Required'}), 401

# Update Customer Endpoint
@api.route('/customers/<id>', methods = ['POST', 'PUT'])
@token_required
def update_customer(current_user_token, id):
    customer = Customer.query.get(id)

    customer.first_name = request.json['first_name']
    customer.last_name = request.json['last_name']
    customer.needle = request.json['needle']
    customer.machine = request.json['machine']
    customer.pigment = request.json['pigment']
    customer.brow_type = request.json['brow_type']
    customer.user_token = current_user_token.token

    db.session.commit()
    response = customer_schema.dump(customer)
    return jsonify(response)

# Delete Customer Endpoint
@api.route('/customers/<id>', methods = ['DELETE'])
@token_required
def delete_customer(current_user_token, id):
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()

    response = customer_schema.dump(customer)
    return jsonify(response)



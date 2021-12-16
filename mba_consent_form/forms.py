from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    email = StringField('Enter Email Address', validators= [DataRequired(), Email()])
    password = PasswordField('Enter Password', validators= [DataRequired()])
    submit_button = SubmitField()

class CreateCustomerForm(FlaskForm):
    first_name = StringField('Enter First Name',validators= [DataRequired()])
    last_name = StringField('Enter Last Name', validators= [DataRequired()])
    needle = StringField('Enter Type of Needle')
    machine = StringField('Enter Type of Machine')
    pigment = StringField('Enter Pigment')
    brow_type = StringField('Enter Brow Type')
    create = SubmitField()

class SearchCustomerForm(FlaskForm):
    first_name = StringField('Enter First Name',validators= [DataRequired()])
    last_name = StringField('Enter Last Name', validators= [DataRequired()])
    Search = SubmitField()

class ConsentForm(FlaskForm):
    first_name = StringField('Enter First Name',validators= [DataRequired()])
    last_name = StringField('Enter Last Name', validators= [DataRequired()])
    address = StringField('Enter Address', validators=[DataRequired()])
    phone_number = StringField('Enter Phone Number', validators=[DataRequired()])
    consent =  StringField('Type Yes to Consent', validators=[DataRequired()])
    submit = SubmitField()

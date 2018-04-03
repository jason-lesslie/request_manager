# from flask_wtf import Form  flask_wtf.Form name changed to flask_wtf.FlaskForm
from flask_wtf import FlaskForm
from wtforms import validators, StringField

class ProductForm(FlaskForm):
    name = StringField('Name', [validators.Required()])

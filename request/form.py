# from flask_wtf import Form  flask_wtf.Form name changed to flask_wtf.FlaskForm
from flask_wtf import FlaskForm
from wtforms import validators, StringField, TextAreaField, SelectField
from wtforms.fields.html5 import DateField

class RequestForm(FlaskForm):
    title = StringField('Title', [
        validators.Required(),
        validators.Length(min=0, max=40)])
    description = TextAreaField('Description', [
        validators.Required(),
        validators.Length(min=20, max=100)])
    target_date = DateField('Target Date', format='%Y-%m-%d')
    product_id = SelectField(u'Product', coerce=int)
    client_id = SelectField(u'Client', coerce=int)
    client_request_priority = SelectField(u'Client Request Priority', coerce=int)

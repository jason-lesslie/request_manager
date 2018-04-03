from request_manager import app, db
from flask import render_template, redirect, url_for
from request.form import RequestForm
from product.models import Product
from client.models import Client
from request.models import RequestModel

@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('request_form_view'))

@app.route('/request_list_view')
def request_list_view():
    all_client_requests = RequestModel.query.all()
    return render_template('request/list_view.html', all_client_requests=all_client_requests)

@app.route('/request_form_view', methods=('GET', 'POST'))
def request_form_view():
    form = RequestForm()
    form.product_id.choices = [(p.id, p.name) for p in Product.query.order_by('name')]
    form.client_id.choices = [(c.id, c.name) for c in Client.query.order_by('name')]
    # # set the default value for client_id to 1 ('Client A'), without this line flask_wtf sets default value to "None"
    form.client_id.data = 1
    client_requests = [r.client_request_priority for r in RequestModel.query.filter(RequestModel.client_id == form.client_id.data)]
    form.client_request_priority.choices = [(x, x) for x in range(1, len(client_requests)+2)]
    if form.validate_on_submit():
        # check if other client priorities need to be updated
        if len(client_requests) >= form.client_request_priority.data:
            db.session.query(RequestModel).filter(RequestModel.client_request_priority >= form.client_request_priority.data).\
                update({"client_request_priority": RequestModel.client_request_priority + 1}, synchronize_session='evaluate')
        request = RequestModel(
            form.title.data,
            form.description.data,
            form.target_date.data,
            form.product_id.data,
            form.client_id.data,
            form.client_request_priority.data
        )
        db.session.add(request)
        # flush() gets mysql to generate an autoincremented user ID
        db.session.flush()
        if request.id:
            db.session.commit()
        else:
            db.session.rollback()
            error = "Error creating request"
        return redirect('/request_list_view')
    return render_template('request/form_view.html', form=form)

@app.route('/request_success')
def request_success():
    return "Request sucess!"

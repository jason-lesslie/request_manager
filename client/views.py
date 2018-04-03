from request_manager import app, db
from flask import render_template, redirect, url_for
from client.form import ClientForm
from client.models import Client

@app.route('/client_list_view')
def client_list_view():
    all_clients = Client.query.all()
    return render_template('client/list_view.html', all_clients=all_clients)

@app.route('/client_form_view', methods=('GET', 'POST'))
def client_form_view():
    form = ClientForm()
    if form.validate_on_submit():
        client = Client(
            form.name.data
        )
        db.session.add(client)
        # flush() gets mysql to generate an autoincremented user ID
        db.session.flush()
        if client.id:
            db.session.commit()
        else:
            db.session.rollback()
            error = "Error creating client"
        return redirect('/client_list_view')
    return render_template('client/form_view.html', form=form)

@app.route('/client_create_success')
def client_create_success():
    return "Client create sucess!"

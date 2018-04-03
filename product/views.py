from request_manager import app, db
from flask import render_template, redirect, url_for
from product.form import ProductForm
from product.models import Product

@app.route('/product_list_view')
def product_list_view():
    all_products = Product.query.all()
    return render_template('product/list_view.html', all_products=all_products)

@app.route('/product_form_view', methods=('GET', 'POST'))
def product_form_view():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            form.name.data
        )
        db.session.add(product)
        # flush() gets mysql to generate an autoincremented user ID
        db.session.flush()
        if product.id:
            db.session.commit()
        else:
            db.session.rollback()
            error = "Error creating product"
        return redirect('/product_list_view')
    return render_template('product/form_view.html', form=form)

@app.route('/product_create_success')
def product_create_success():
    return "Product create sucess!"

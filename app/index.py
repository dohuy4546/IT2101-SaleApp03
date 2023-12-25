import math
from flask import Flask, render_template, request, redirect, session, jsonify
import dao
from app import app, login, utils
from flask_login import login_user

@app.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')
    cates = dao.get_categories()
    products = dao.get_products(kw, cate_id, page)
    num = dao.count_product()
    page_size = app.config['PAGE_SIZE']
    return render_template('index.html', categories=cates, products=products, page= math.ceil(num/page_size))

@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
    else:
        return render_template('admin/index.html', err=True)
    return redirect('/admin')

@app.route('/api/cart', methods=['post'])
def add_to_cart():
    """
    {
        "cart": {
            "1": {
                "id": "1",
                "name": "ABC",
                "price": 12,
                "quantity": 2
            }, "2": {
                "id": "2",
                "name": "ABC",
                "price": 12,
                "quantity": 1
            }
        }
    }
    :return:
    """
    data = request.json

    cart = session.get('cart')
    if cart is None:
        cart = {}

    id = str(data.get("id"))
    if id in cart: # sp da co trong gio
        cart[id]['quantity'] += 1
    else: # sp chua co trong gio
        cart[id] = {
            "id": id,
            "name": data.get('name'),
            "price": data.get('price'),
            "quantity": 1
        }

    session['cart'] = cart
    print(utils.count_cart(cart))
    return jsonify(utils.count_cart(cart))

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/api/cart/<product_id>', methods=['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/api/cart/<product_id>', methods=['delete'])
def delete_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        del cart[product_id]

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

@app.context_processor
def common_response():
    return {
        'categories': dao.get_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
from flask import Flask, render_template
from api.user_api import get_users
from api.product_api import get_products
from api.order_api import get_orders

app = Flask(__name__)

@app.route('/')
def index():
    users = get_users()
    products = get_products()
    orders = get_orders()
    return render_template('index.html', users=users, products=products, orders=orders)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

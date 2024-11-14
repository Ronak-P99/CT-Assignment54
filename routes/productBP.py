from flask import Blueprint
from controllers.productController import save, find_all_pagination, find_all, get_max_orders

product_bluprint = Blueprint('product_bp', __name__)
product_bluprint.route('/', methods=['POST'])(save)
product_bluprint.route('/paginate', methods=['GET'])(find_all_pagination)
product_bluprint.route('/', methods=['GET'])(find_all)
product_bluprint.route('/product-max', methods=['GET'])(get_max_orders)

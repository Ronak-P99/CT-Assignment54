from flask import Blueprint
from controllers.productController import save, find_all

product_bluprint = Blueprint('product_bp', __name__)
product_bluprint.route('/', methods=['POST'])(save)
product_bluprint.route('/', methods=['GET'])(find_all)

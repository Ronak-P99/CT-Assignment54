from flask import Blueprint
from controllers.orderController import save, find_all

order_bluprint = Blueprint('order_bp', __name__)
order_bluprint.route('/', methods=['POST'])(save)
order_bluprint.route('/', methods=['GET'])(find_all)

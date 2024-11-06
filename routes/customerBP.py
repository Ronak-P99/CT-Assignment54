from flask import Blueprint
from controllers.customerController import save, find_all

customer_bluprint = Blueprint('customer_bp', __name__)
customer_bluprint.route('/', methods=['POST'])(save)
customer_bluprint.route('/', methods=['GET'])(find_all)

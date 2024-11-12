from flask import Blueprint
from controllers.customerController import save, find_all, find_customers_gmail, find_all_pagination

customer_bluprint = Blueprint('customer_bp', __name__)
customer_bluprint.route('/', methods=['POST'])(save)
customer_bluprint.route('/', methods=['GET'])(find_all)
customer_bluprint.route('/gmail', methods=['GET'])(find_customers_gmail)
customer_bluprint.route('/paginate', methods=['GET'])(find_all_pagination)

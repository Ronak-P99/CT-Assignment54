from flask import Blueprint
from controllers.orderController import save, find_by_id, find_all_pagination, find_all

order_bluprint = Blueprint('order_bp', __name__)
order_bluprint.route('/', methods=['POST'])(save)
order_bluprint.route('/id/<int:id>', methods=['GET'])(find_by_id)
order_bluprint.route('/paginate', methods=['GET'])(find_all_pagination)
order_bluprint.route('/', methods=['GET'])(find_all)

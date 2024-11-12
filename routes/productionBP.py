from flask import Blueprint
from controllers.productionController import save, find_all

production_bluprint = Blueprint('production_bp', __name__)
production_bluprint.route('/', methods=['POST'])(save)
production_bluprint.route('/', methods=['GET'])(find_all)
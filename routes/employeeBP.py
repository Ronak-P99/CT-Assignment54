from flask import Blueprint
from controllers.employeeController import save, find_all

employee_bluprint = Blueprint('employee_bp', __name__)
employee_bluprint.route('/', methods=['POST'])(save)
employee_bluprint.route('/', methods=['GET'])(find_all)

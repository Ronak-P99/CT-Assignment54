from flask import Flask
from database import db 
from schema import ma
from limiter import limiter
from caching import cache

from models.customer import Customer
from models.customerAccount import CustomerAccount
from models.employee import Employee
from models.order import Order
from models.product import Product
from models.production import Production

from routes.customerBP import customer_bluprint
from routes.employeeBP import employee_bluprint
from routes.orderBP import order_bluprint
from routes.productBP import product_bluprint
from routes.productionBP import production_bluprint


def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)

    return app

def blue_print_config(app):
    app.register_blueprint(customer_bluprint, url_prefix='/customers')
    # /customers
    # Because of the blueprint, the '/' would come after '/customers'. Whatever you put in the bluprint would be added after '/customers'
    # '/customers/' 
    app.register_blueprint(employee_bluprint, url_prefix='/employees')
    app.register_blueprint(order_bluprint, url_prefix='/orders')
    app.register_blueprint(product_bluprint, url_prefix='/products')
    app.register_blueprint(production_bluprint, url_prefix='/productions')




def configure_rate_limit():
    limiter.limit("5 per day")(customer_bluprint)
    limiter.limit("5 per day")(order_bluprint)
    limiter.limit("5 per day")(employee_bluprint)
    limiter.limit("5 per day")(product_bluprint)
    limiter.limit("5 per day")( production_bluprint)

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blue_print_config(app)
    configure_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True)
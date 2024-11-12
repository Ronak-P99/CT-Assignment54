from flask import Flask
from database import db 
from schema import ma
from limiter import limiter
from caching import cache
from sqlalchemy.orm import Session


from models.customer import Customer
from models.customerAccount import CustomerAccount
from models.order import Order
from models.product import Product
from models.production import Production
from models.employee import Employee
from models.order_product import order_product

from routes.customerBP import customer_bluprint
from routes.orderBP import order_bluprint
from routes.productBP import product_bluprint
from routes.customerAccountBP import customer_account_blueprint
from routes.productionBP import production_bluprint
from routes.employeeBP import employee_bluprint



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
    app.register_blueprint(order_bluprint, url_prefix='/orders')
    app.register_blueprint(product_bluprint, url_prefix='/products')
    app.register_blueprint(customer_account_blueprint, url_prefix='/accounts')
    app.register_blueprint(production_bluprint, url_prefix='/productions')
    app.register_blueprint(employee_bluprint, url_prefix='/employees')






def configure_rate_limit():
    limiter.limit("5 per day")(customer_bluprint)

def init_customers_info_data():
    with Session(db.engine) as session:
        with session.begin():
            customers = [
                Customer(name="Customer One", email="customer1@example.com",phone="092319283"),
                Customer(name="Customer Two", email="customer2@gmail.com",phone="092319283"),
                Customer(name="Customer Three", email="customer3@hotmail.com",phone="092319283"),
            ]
            customersAccounts = [
                CustomerAccount(username="ctm1", password="password1",customer_id=1),
                CustomerAccount(username="ctm2", password="password2",customer_id=2),
                CustomerAccount(username="ctm3", password="password3",customer_id=3),
            ]
            products = [
                Product(name="Product One", price=9.99),
                Product(name="Product Two", price=12.99),
                Product(name="Product Three", price=10.99),
            ]
            orders = [
                Order(date="1234-11-12", customer_id=1),
                Order(date="1234-11-13", customer_id=2),
                Order(date="1234-11-14", customer_id=3),
            ]
            session.add_all(customers)
            session.add_all(customersAccounts)
            session.add_all(products)
            session.add_all(orders)


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blue_print_config(app)
    configure_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()
        init_customers_info_data()

    app.run(debug=True)
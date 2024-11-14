from sqlalchemy.orm import Session
from database import db
from models.product import Product
from sqlalchemy import select, func
from models.order import Order
def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit() 
        session.refresh(new_product)
        return new_product
        
def find_all_pagination(page=1, per_page=10):
    products = db.paginate(select(Product), page=page, per_page=per_page)
    return products

def find_all():
    query = select(Product)
    products = db.session.execute(query).scalars().all()
    return products

def get_max_orders():
   # Query to calculate total production per employee
    results = db.session.query(
        Product.name,
        func.sum(Product.quantity_ordered).label('total_quantity_ordered')
    ).join(Order, Order.id == Product.order_id) \
    .group_by(Product.name).order_by(func.sum(Product.quantity_ordered).desc()).all()

    return [{'product_name': name, 'total_quantity_ordered': total} for name, total in results]

from marshmallow import fields, validate
from schema import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    quantity = fields.Integer(required=True)
    total_price = fields.Float(required=True, validate=validate.Range(min=0))
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
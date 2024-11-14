from marshmallow import fields, validate
from schema import ma

class ProductionSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True, validate=validate.Length(min=1))
    quantity_produced = fields.Integer(required=True)
    date_produced = fields.Date(required=True)
    product_id = fields.Integer(required=True)
    emplyee_name = fields.String(required=True)

production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True)
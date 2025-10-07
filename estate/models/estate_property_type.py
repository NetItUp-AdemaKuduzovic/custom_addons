from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    _order = 'name'
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The name of the property type must be unique!'),
    ]

    property_ids = fields.One2many('estate.property', 'property_type_id', string='Types')
    
    name=fields.Char(required=True)

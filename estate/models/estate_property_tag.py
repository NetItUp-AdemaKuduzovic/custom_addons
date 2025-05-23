from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'
    _order = "name"
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The name of the property type must be unique!'),
    ]

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color Index')
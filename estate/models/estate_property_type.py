from odoo import models, fields

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    
    name=fields.Char(required=True)
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

    def action_open_property_ids(self):
        return {
            "name": "Related properties",
            "type": "ir.actions.act.window",
            "view_mode": "list, form", 
            "res_model": "estate.property",
            "target": "current",
            "domain": [("property_type_id", "=", self.id)],
            "context": {"default_property_type_id": self.id}
        }

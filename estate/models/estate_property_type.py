from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    _order = 'name'
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The name of the property type must be unique!'),
    ]

    property_ids = fields.One2many('estate.property', 'property_type_id', string='Types')
    name=fields.Char(required=True)
    property_count = fields.Integer(compute="_compute_property_count")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list: 
            self.env['estate.property.tag'].create(
                {
                    "name": vals.get("name")
                }
            )
        return super().create(vals_list)
    
    def unlink(self):
        self.property_ids.state = 'cancelled'
        return super().unlink()

    @api.depends("property_ids")
    def _compute_property_count(self):
        for rec in self: 
            rec.property_count = len(rec.property_ids)

    def action_open_property_ids(self):
        return {
            "name": "Related properties",
            "type": "ir.actions.act_window",
            "view_mode": "list,form", 
            "res_model": "estate.property",
            "target": "current",
            "domain": [("property_type_id", "=", self.id)],
            "context": {"default_property_type_id": self.id}
        }

from odoo import fields, models, api

class newService(models.Model):
    _name = "new_timesheet.service"
    _description = "Services from eSolver"

    _sql_constraints = [
        ('unique_short_code', 'unique(short_code)', 'The short code must be unique.')
    ]

    name = fields.Char(compute="_compute_name", store=True)
    short_code = fields.Char(required = True, string="Code")
    description = fields.Text(required = True)

    @api.depends("short_code", "description")
    def _compute_name(self):
        for record in self:
            record.name = f"{record.short_code} - {record.description}"

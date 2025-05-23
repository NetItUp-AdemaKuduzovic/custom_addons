from odoo import models, fields, api
from datetime import timedelta

class estatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float()
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status', copy=False)
    validity = fields.Integer(string='Validity (days)', default=7) 
    date_deadline = fields.Date(string="Deadline", compute="_compute_deadline_date", inverse="_inverse_deadline_date",store=True)

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)

    @api.depends('validity')
    def _compute_deadline_date(self): 
        for rec in self:
            if rec.validity and rec.create_date:
                rec.date_deadline = rec.create_date + timedelta(days=rec.validity)
            else:
                rec.date_deadline = False

    @api.onchange('date_deadline')
    def _inverse_deadline_date(self):
        for rec in self:
            if rec.validity and rec.create_date:
                rec.validity = (rec.date_deadline - rec.create_date.date()).days
            else:
                rec.validity = 0

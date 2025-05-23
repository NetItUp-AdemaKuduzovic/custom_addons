from odoo import models, fields, api
from datetime import timedelta

class estatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'
    _order = 'price desc'
    _sql_constraints = [
        ('price_positive', 'check(price > 0)', 'The price must be positive.')
    ]

    price = fields.Float()
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status', copy=False)
    validity = fields.Integer(string='Validity (days)', default=7) 
    date_deadline = fields.Date(string='Deadline', compute='_compute_deadline_date', inverse='_inverse_deadline_date',store=True)

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)

    @api.depends('validity')
    def _compute_deadline_date(self): 
        for rec in self:
            if rec.create_date:
                rec.date_deadline = rec.create_date + timedelta(days=rec.validity)
            else:
                rec.date_deadline = fields.Date.today() + timedelta(days=rec.validity)

    @api.onchange('date_deadline')
    def _inverse_deadline_date(self):
        for rec in self:
            if rec.validity and rec.create_date:
                rec.validity = (rec.date_deadline - rec.create_date.date()).days

    def action_refuse_offer(self):
        for rec in self:
            rec.status = 'refused'

    @api.constrains('expected_price')
    def action_accept_offer(self):
        for rec in self:
            if rec.price >= 9/10 * rec.property_id.expected_price:
                rec.status = 'accepted'
                rec.property_id.state = 'offer_accepted'
                rec.property_id.selling_price = rec.price
                rec.property_id.buyer_id = rec.partner_id
                return True
            else:
                raise models.ValidationError('The offer must be at least 90% of the expected price.')

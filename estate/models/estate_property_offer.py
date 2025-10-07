from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta

class EstatePropertyOffer(models.Model):
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
    property_type_id = fields.Many2one(related='property_id.property_type_id', store=True)

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
        self.ensure_one()
        if "accepted" in self.property_id.offer_ids.mapped('status'):
            raise UserError("One offer was already accepted.")

        if self.price >= 9/10 * self.property_id.expected_price:
            self.status = 'accepted'
            self.property_id.state = 'offer_accepted'
            self.property_id.selling_price = self.price
            self.property_id.buyer_id = self.partner_id
            return True
        else:
            raise models.ValidationError('The offer must be at least 90% of the expected price.')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'property_id' in vals:
                property_rec = self.env['estate.property'].browse(vals['property_id'])
                property_rec.state = 'offer_received'
                
                existing_offers = property_rec.offer_ids.mapped('price')
                max_existing_price = max(existing_offers, default=0.0)
                
                if vals.get('price', 0) <= max_existing_price:
                    raise models.ValidationError('The offer price must be higher than the existing offers.')
        return super(EstatePropertyOffer, self).create(vals)
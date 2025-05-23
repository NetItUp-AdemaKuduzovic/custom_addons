from odoo import fields, models, api
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

class estateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'
    _order = 'sequence, id desc'
    _sql_constraints = [
        ('expected_price_positive', 'check(expected_price >= 0)', 'The expected price must be positive or null.'),
        ('selling_price_positive', 'check(selling_price >= 0)', 'The selling price must be positive or null.')
    ]
    
    name = fields.Char(required=True, default='Unknown')
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, string='Available From', default=lambda self: fields.Date.today()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (sqm)')
    active = fields.Boolean(default=True)
    total_area = fields.Float(compute='_compute_total_area', string='Total Area (sqm)')
    best_offer = fields.Float(compute='_compute_best_offer')
    sequence = fields.Integer(string='Sequence', default=1, help='Used to order the properties list view. Lower is better.')
    garden_orientation = fields.Selection([
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ], 'Garden Orientation')
    last_seen = fields.Datetime('Last Seen', default=fields.Datetime.now)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer received'),
        ('offer_accepted', 'Offer accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),
    ],'State', required=True,copy=False,default='new')

    property_type_id = fields.Many2one('estate.property.type', string='Property Type', options={'can_create': False, 'can_write': False})
    buyer_id = fields.Many2one('res.partner',string='Buyer', copy=False)
    seller_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for rec in self:
            rec.best_offer = max(rec.offer_ids.mapped('price'), default=0.0)    

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    def action_set_sold(self):
        for rec in self:
            if rec.state == 'cancelled':
                raise UserError('Cancelled properties cannot be sold')
            rec.state = 'sold'

    def action_set_cancelled(self):
        for rec in self:
            if rec.state == 'sold' or rec.state == 'offer_accepted':
                raise UserError('Sold properties cannot be cancelled')
            rec.state = 'cancelled'


    # def _get_default_seller_id1(self):
    #     return self.env.user
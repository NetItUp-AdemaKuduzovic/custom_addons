from odoo import models, fields, api
from datetime import datetime, timedelta
import pytz

class NiuStamping(models.Model):
    _name = 'niu.stamping'
    _description = 'Niu Stamping'
    _order = "stamping_timestamp desc"

    active = fields.Boolean(string="Active", default=True)
    stamping_timestamp = fields.Datetime(string='Timestamp', required=True, default=lambda self: fields.Datetime.now())

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    badge_id = fields.Char(string="Badge ID", store=True)
    niu_attendance_id = fields.Many2one('niu.attendance', string='Related Attendance')

    stamping_direction = fields.Selection([
        ('in', 'Check-In'),
        ('out', 'Check-Out')
    ], string='Stamping Direction', required=False)
    hour = fields.Char(string="Stamping time", compute="_compute_time_only")

    @api.depends('stamping_timestamp')
    def _compute_time_only(self):
        user_tz = self.env.user.tz or 'UTC'
        tz = pytz.timezone(user_tz)
        for record in self: 
            if record.stamping_timestamp:
                localized_dt = pytz.utc.localize(record.stamping_timestamp).astimezone(tz)
                record.hour = localized_dt.strftime('%H:%M:%S')

            else: 
                record.hour = ''

    def _get_employee_id(self): 
        # Based on badge-id used for stamping: get employee_id
        employee_id = self.env['hr.employee'].search([('barcode', '=', self.badge_id)], limit=1)
        return employee_id.id if employee_id else False
    
    @api.onchange('badge_id')
    def _onchange_badge_id(self):
        for record in self:
            record.employee_id = record._get_employee_id()

    @api.model
    def create(self, vals):
        # Stamping will be created from an endpoint
        niu_attendance_id = self.env['niu.attendance'].search([
            ('attendance_date', '=', datetime.strptime(vals.get('stamping_timestamp'), "%Y-%m-%d %H:%M:%S").date()),
            ('employee_id', '=', vals.get('employee_id'))
        ])
        vals['niu_attendance_id'] = niu_attendance_id.id if niu_attendance_id else False

        number_of_stampings = self.search_count([
            ('employee_id', '=', vals.get('employee_id')),
            ('stamping_timestamp', '>=', datetime.strptime(vals.get('stamping_timestamp'), "%Y-%m-%d %H:%M:%S").date()),
            ('stamping_timestamp', '<=', datetime.strptime(vals.get('stamping_timestamp'), "%Y-%m-%d %H:%M:%S").date() + timedelta(days=1))
        ])
        if number_of_stampings % 2 == 0:
            vals['stamping_direction'] = 'in'
        else:
            vals['stamping_direction'] = 'out'
        
        return super().create(vals)
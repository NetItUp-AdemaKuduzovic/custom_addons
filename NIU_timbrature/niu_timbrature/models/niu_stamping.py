from odoo import models, fields, api
from datetime import datetime, date, timedelta

class NiuStamping(models.Model):
    _name = 'niu.stamping'
    _description = 'Niu Stamping'

    active = fields.Boolean(string="Active", default=True)
    stamping_timestamp = fields.Datetime(string='Timestamp', required=True, default = fields.Date.today())

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    badge_id = fields.Char(string="Badge ID", store=True)
    niu_attendance_id = fields.Many2one('niu.attendance', string='Related Attendance')

    stamping_direction = fields.Selection([
        ('in', 'Check-In'),
        ('out', 'Check-Out')
    ], string='Stamping Direction', required=True)

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
        return super().create(vals)

    
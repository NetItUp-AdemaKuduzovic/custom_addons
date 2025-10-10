from odoo import models, fields, api

class NiuStamping(models.Model):
    _name = 'niu.stamping'
    _description = 'Niu Stamping'

    name = fields.Char(string='Stamping Name', compute='_compute_name', store=True)
    active = fields.Boolean(string="Active", default=True)
    stamping_timestamp = fields.Datetime(string='Timestamp', required=True)

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    badge_id = fields.Char(string="Badge ID", related='employee_id.barcode', store=True)
    niu_attendance_id = fields.Many2one('niu.attendance', string='Related Attendance')

    stamping_direction = fields.Selection([
        ('in', 'Check-In'),
        ('out', 'Check-Out')
    ], string='Stamping Direction', required=True)

    @api.model
    def create_stamping(self, vals):
        return self.create(vals)

    @api.depends('employee_id', 'stamping_timestamp', 'stamping_direction')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.employee_id.name} - {record.stamping_timestamp} - {record.stamping_direction}"

    
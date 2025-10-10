from odoo import models, fields, api

class NiuAttendance(models.Model):
    _name = 'niu.attendance'
    _description = 'Niu Attendance'

    name = fields.Char(string="Attendance Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    attendance_date = fields.Datetime(string="Attendance Date", required=True)

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    niu_stamping_ids = fields.One2many('niu.stamping', 'niu_attendance_id', string='Related Stampings')

    @api.model
    def _generate_attendances(self):
        # Method called from cron job to generate new attendances every day at midnight, then stampings get populated into them from controller
        today = fields.Date.context_today(self)
        existing_attendances = self.search([('attendance_date', '>=', today), ('attendance_date', '<', today + fields.Date.timedelta(days=1))])
        if not existing_attendances:
            employees = self.env['hr.employee'].search([])
            for employee in employees:
                self.create({
                    'name': f'Attendance for {employee.name} on {today}',
                    'attendance_date': today,
                    'employee_id': employee.id,
                })  
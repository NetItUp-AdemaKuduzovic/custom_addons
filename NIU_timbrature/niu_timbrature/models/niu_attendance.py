from odoo import models, fields, api

class NiuAttendance(models.Model):
    _name = 'niu.attendance'
    _description = 'Niu Attendance'

    name = fields.Char(string="Attendance Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    attendance_date = fields.Date(string="Attendance Date", required=True)

    day = fields.Char()
    first_in = fields.Datetime(string="Morning In")
    first_out = fields.Datetime(string="Morning Out")
    second_in = fields.Datetime(string="Afternoon In")
    second_out = fields.Datetime(string="Afternoon Out")

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    niu_stamping_ids = fields.One2many('niu.stamping', 'niu_attendance_id', string='Related Stampings')

    @api.model
    def _generate_attendances(self):
        # Method called from cron job to generate new attendances every day at midnight, then stampings get populated into them from controller
        # Make a set of of all attendances, employee for a date, then search if existant, if not create one 
        today = fields.Date.context_today(self)
        existing_attendances = self.search([('attendance_date', '=', today), ('employee_id', '=', employee.id)])
        if not existing_attendances:
            employees = self.env['hr.employee'].search([])
            for employee in employees:
                self.create({
                    'name': f'Attendance for {employee.name} on {today}',
                    'attendance_date': today,
                    'employee_id': employee.id,
                })  
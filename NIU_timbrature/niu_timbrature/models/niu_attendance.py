from odoo import models, fields, api
import datetime

class NiuAttendance(models.Model):
    _name = 'niu.attendance'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Niu Attendance'
    _order = 'attendance_date asc'

    name = fields.Char(string="Attendance Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    attendance_date = fields.Date(string="Attendance Date", required=True)

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    badge_id = fields.Char(related="employee_id.barcode", string="Badge ID")
    niu_stamping_ids = fields.One2many('niu.stamping', 'niu_attendance_id', string='Related Stampings', tracking=True)
    is_valid = fields.Boolean(string="Valid Attendance", default=True)

    @api.model
    def _generate_attendances(self):
        today = fields.Date.today()
        
        existing_attendances = {
            rec["employee_id"][0]
            for rec in self.env['niu.attendance'].search_read(
                [('attendance_date', '=', today)], ['employee_id']
            )
        }
        
        employees = self.env['hr.employee'].search([])

        to_create = [
            {
                'name': f'Attendance for {employee.name} on {today}',
                'attendance_date': today,
                'employee_id': employee.id,
            }
            for employee in employees
            if employee.id not in existing_attendances
        ]

        # Create attendances in batch
        if to_create:
            self.env['niu.attendance'].create(to_create)

    @api.model
    def _check_attendance_validity(self):
        today = fields.Date.today()

        attendances = self.env['niu.attendance'].search([('attendance_date', '=', today)])

        for attendance in attendances:
            if (len(attendance.niu_stamping_ids) > 6 or
                len(attendance.niu_stamping_ids) % 2 != 0): 
                attendance.is_valid = False
                continue

            # for i in range(len(attendance.niu_stamping_ids) - 2):
            #     if attendance[i+1] - attendance[i] < datetime.timedelta(seconds = 90):
            #         attendance.is_valid = False
            #         break



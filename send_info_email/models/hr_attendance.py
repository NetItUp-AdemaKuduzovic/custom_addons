from odoo import models, api

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    #Overrides
    @api.model_create_multi
    def create(self, vals_list):
        attendances = super().create(vals_list)
        attendances._send_attendance_email('created')
        return attendances

    def write(self, vals):
        old_values= {}
        if 'check_in' in vals:
            old_values.update({'check_in': self.check_in})
        if 'check_out' in vals:
            old_values.update({'check_out': self.check_out})
  
        res = super().write(vals)

        if 'check_in' in vals or 'check_out' in vals :
            self._send_attendance_email('edited', old_values)
        
        return res

    def unlink(self):
        self._send_attendance_email('deleted')
        res = super().unlink()
        return res

    def _send_attendance_email(self, action, old_values=None):
        """
        Send informative email to an employee when his check in or check out time changes in his attendance record
        """
        for record in self:
            if record.employee_id.receive_email:
                template = self.env.ref('send_info_email.attendance_email_notification_template')

                context = {
                    'action': action,
                    'old_values': old_values
                }
                template.with_context(context).send_mail(record.id)
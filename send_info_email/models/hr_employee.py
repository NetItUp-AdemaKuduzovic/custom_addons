# Here i should inherit class hr_employee and add a field 
# After adding a field, I sh
from odoo import fields,models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    receive_email = fields.Boolean(
        string="Receive emails", 
        help="Receive informative emails about my attendance changes."
    )
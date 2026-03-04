from odoo import models, fields

class HostelStudent(models.Model):
    _name = 'hostel.student'
    _inherits = {'res.partner': 'partner_id'}
    _description = "Hostel Student Information"

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ], string="Gender", help="Student Gender")
    
    room_id = fields.Many2one("hostel.room", "Room", help="Select hostel room")
    hostel_id = fields.Many2one("hostel.hostel", related="room_id.hostel_id")
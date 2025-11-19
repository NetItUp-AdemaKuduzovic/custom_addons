from odoo import fields, models

class HostelRoom(models.Model):
    _name = "hostel.room"

    name = fields.Char(string="Name")
    room_number = fields.Integer(string="Room No.")
    floor_number = fields.Integer(string="Floor No.")
    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_amount = fields.Monetary(string="Rent Amount", help="Enter rent amount per month")

    hostel_id = fields.Many2one("hostel.hostel", "hostel", help="Name of hostel")
    student_ids = fields.One2many("hostel.student", "room_id", string="Students", help="Enter students")
    hostel_amenities_ids = fields.Many2many("hostel.amenities", "hostel_room_amenities_rel", "room_id", "amenity_id", 
        string="Amenities", domain="[('active', '=', 'True')]", help="Select hostel room amenities")
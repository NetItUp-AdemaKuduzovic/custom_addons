from odoo import _,api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _
from datetime import timedelta

class HostelRoom(models.Model):
    _name = "hostel.room"
    _sql_constraints = [("room_number_unique", "unique(room_number)", "Room number must be unique")]

    name = fields.Char(string="Name")
    room_number = fields.Integer(string="Room No.")
    floor_number = fields.Integer(string="Floor No.")
    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_amount = fields.Monetary(string="Rent Amount", help="Enter rent amount per month")
    student_per_room = fields.Integer("Student per Room", required=True, help="Students allocated per room")
    availability = fields.Float(compute = "_compute_check_availability", string="Availability", help="Room availability in hostel", store=True)
    admission_date = fields.Date("Admission Date", help="Date of admission in hostel", default=fields.Datetime.today)
    discharge_date = fields.Date("Discharge Date", help="Date on which student discharges")
    duration = fields.Integer("Duration", compute="_compute_check_duration", inverse="_inverse_duration", help="Enter duration of living")
    state = fields.Selection(
        [('unavailable', 'Unavailable'),
        ('available', 'Available'),
        ('closed', 'Closed')],
        'State', default="unavailable"
    )

    hostel_id = fields.Many2one("hostel.hostel", "hostel", help="Name of hostel")
    student_ids = fields.One2many("hostel.student", "room_id", string="Students", help="Enter students")
    hostel_amenities_ids = fields.Many2many("hostel.amenities", "hostel_room_amenities_rel", "room_id", "amenity_id", 
        string="Amenities", domain="[('active', '=', 'True')]", help="Select hostel room amenities")
    
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [
            ('unavailable', 'available'),
            ('available', 'closed'),
            ('closed', 'unavailable')
        ]
        return (old_state, new_state) in allowed
    
    def change_state(self, new_state):
        for room in self: 
            if room.is_allowed_transition(room.state, new_state):
                room.state = new_state
            else:
                msg = _('Moving from %s to %s state is not allowed') % (room.state, new_state)
                raise UserError(msg)

    def make_available(self):
        self.change_state('available')
    
    def make_closed(self):
        self.change_state('closed')
    
    @api.depends("admission_date", "discharge_date")
    def _compute_check_duration(self):
        for rec in self:
            if rec.discharge_date and rec.admission_date:
                rec.duration = (rec.discharge_date - rec.admission_date).days
    
    def _inverse_duration(self):
        for stu in self:
            if stu.discharge_date and stu.admission_date:
                duration = (stu.discharge_date - stu.admission_date).days

                if duration != stu.duration:
                    stu.discharge_date = (stu.admission_date + timedelta(days=stu.duration)).strftime('%Y-%m-%d')

    @api.depends("student_per_room", "student_ids")
    def _compute_check_availability(self):
        for rec in self:
            rec.availability = rec.student_per_room - len(rec.student_ids.ids)
    
    @api.constrains("rent_amount")
    def _check_rent_amount(self):
        if self.rent_amount < 0:
            raise ValidationError(_("Rent Amount per Month should not be a negative value!"))
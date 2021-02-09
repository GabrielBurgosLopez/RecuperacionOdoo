from odoo import models, fields

class Natural_Park(models.Model):
    _name = 'naturalparks.natural_park'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    starting_date = fields.Date()
    extension = fields.Integer(string="Extension (in km2)", required=True)

    community_ids = fields.Many2many('naturalparks.community', string="Autonomous Communities", required=True)

    
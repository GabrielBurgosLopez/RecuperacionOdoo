from odoo import models, fields

class Acommodation(models.Model):
    _name = 'naturalP.acommodation'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(required=True)
    category = fields.Selection([('one', '*'), ('two','**'), ('three', '***'), ('four', '****'), ('five', '*****')])
    color = fields.Integer()
    
    natural_park_id = fields.Many2one('naturalP.natural_park', string="Natural Park", ondelete='cascade', required=True)

    

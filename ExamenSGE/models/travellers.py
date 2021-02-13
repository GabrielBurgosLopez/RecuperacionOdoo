from odoo import models, fields, api, exceptions

class Visitor(models.Model):
    _name = 'naturalparks.visitor'
    _order = 'name'

    name = fields.Char(required=True)    
    dni = fields.Char(required=True)
    address = fields.Char()
    job = fields.Char()
    natural_park_id = fields.Many2one('naturalparks.natural_park', string="Natural Park", ondelete='cascade', required=True)
    acommodation_id = fields.Many2one('naturalparks.acommodation', string="Acommodation", required=True)
    management_id = fields.Many2one('naturalparks.management', string="Person who registered this visitor")
    color = fields.Integer()
    state = fields.Selection([('1.draft', 'Draft'),('2.confirm', 'Confirm'), ('3.done', 'Done'),], string='Status', default='1.draft')
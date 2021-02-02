from odoo import models, fields, api

class InheritTest(models.Model):
    _inherit = 'res.partner'

    another_test_field = fields.Many2many(string='Hello! I am a new field!')
    test_field = fields.Many2many(comodel_name='academy.course', string='Inherit field')
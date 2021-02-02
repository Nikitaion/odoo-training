from odoo import models, fields, api

class InheritTest(models.Model):
    _inherit = 'res.partner'

    test_field = fields.Many2many(comodel_name='academy.course', string='Inherit field')
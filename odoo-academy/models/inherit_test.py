from odoo import models, fields, api

class InheritTest(models.Model):
    _inherit = 'res.partner'

    another_test_field = fields.Many2many('stock.picking', string="Return Orders")
    test_field = fields.Many2many(comodel_name='academy.course', string='Inherit field')
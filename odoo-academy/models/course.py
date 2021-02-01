# -*- coding: utf-8 -*-

from odoo import models, fields

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Test academy courses'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    level = fields.Selection([('beginner', 'Beginner'),('intermediate', 'Intermediate'),('professional', 'Professional')])
    active = fields.Boolean(string='Is active', default=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ], default='draft')

    def confirm(self):
        self.write({'state':'confirmed'})

    def cancel(self):
        self.write({'state':'canceled'})
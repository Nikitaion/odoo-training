# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Test academy courses'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    level = fields.Selection([('beginner', 'Beginner'),('intermediate', 'Intermediate'),('professional', 'Professional')])
    active = fields.Boolean(string='Is active', default=True)

    start_date = fields.date(string='Start date', default=fields.Date.context_today)
    end_date = fields.date(string='End date')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ], default='draft')

    def confirm(self):
        self.write({'state':'confirmed'})

    def cancel(self):
        self.write({'state':'canceled'})

    # @api.onchange()
    # def changeDate(self):
    #     func
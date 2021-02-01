# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Test academy courses'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    level = fields.Selection([('beginner', 'Beginner'),('intermediate', 'Intermediate'),('professional', 'Professional')])
    active = fields.Boolean(string='Is active', default=True)

    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ], default='draft')

    def confirm(self):
        self.write({'state':'confirmed'})

    def cancel(self):
        self.write({'state':'canceled'})

    @api.onchange('start_date')
    def changeDate(self):
        if self.start_date:
            self.end_date = self.start_date + relativedelta(months=1)

    @api.constrains('name')
    def errorIfConstrains(self):
        if self.search(['&', ('name', '=', self.name), ('id', '!=', self.id)]):
            raise ValidationError("You already have course with same name!")

        # for existingName in self.name:
        #     if (self.name == existingName.name) and (rec.name != self.name):
        #         raise ValidationError("You already have course with same name!")

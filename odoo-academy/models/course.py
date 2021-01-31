# -*- coding: utf-8 -*-

from odoo import models, fields

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course info'

    name = fields.Char(string='Student name', required=True)
    description = fields.String(string='About student')
    level = fields.Selection([('beginner', 'Beginner'),('intermediate', 'Intermediate'),('professional', 'Professional')])
    active = fields.Boolean(string='Is active', default=True)
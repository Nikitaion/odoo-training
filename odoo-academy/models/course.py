# -*- coding: utf-8 -*-

from odoo import models, fields

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course info'
    _inherit = ['mail.thread']

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    level = fields.Selection([('beginner', 'Beginner'),('intermediate', 'Intermediate'),('professional', 'Professional')])
    active = fields.Boolean(string='Is active', default=True)
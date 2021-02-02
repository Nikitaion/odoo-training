from odoo import models, fields, api

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Exercise 2'

    _inherits = {'academy.course':'name'}
    #name in inherits and name in many2one should be same name.(Here it's name from academy.course(course name))
    name = fields.Many2one(comodel_name='academy.course', string='Course name')

    name_of_session = fields.Char(string='Title', required=True)


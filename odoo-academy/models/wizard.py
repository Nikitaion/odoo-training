from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'academy.wizard'

    name = fields.Char()

    course_id = fields.Many2one('academy.course')

    @api.model
    def default_get(self, fields):
        record = super().default_get(fields)
        record['course_id'] = self._context.get('active_id')
        return record

    def update_name(self):
        self.course_id.name = self.name


# class Wizard(models.TransientModel):
#     _name = 'academy.wizard'
#
#     name = fields.Char()
#
#     attendee_id = fields.Many2one('academy.student')
#
#     mobile = fields.Char()
#
#     def add_mobile(self):
#         self.attendee_id.mobile = self.mobile
#         # self.attendee_id.write({ #write can modify one or many records
#         #     'mobile': self.mobile,
#         #     'name': self.attendee_id.name + 'modified'
#         # })
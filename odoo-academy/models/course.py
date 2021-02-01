# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Test academy courses'


    teacher_id = fields.Many2one(comodel_name='academy.teacher', string='Course teacher')


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
    def errorIfConstrains(self): #if ...
        if self.search(['&', ('name', '=', self.name), ('id', '!=', self.id)]):
            raise ValidationError("You already have course with same name!")

    class Student(models.Model):
        _name = 'academy.student'

        level = fields.Selection([('level 1', 'level 1'),('level 2', 'level 2')])
        subject_ids = fields.Many2many(comodel_name='academy.subject', domain="[('level', '=', 'level 2')]")

        course_id = fields.Many2one(comodel_name='academy.course')

        #course_name = fields.Char(related='course_id.name') #when value course changed - this value changed too

        course_teacher = fields.Many2one(related='course_id.teacher_id')

        teacher_ids = fields.One2many(comodel_name='academy.teacher', inverse_name='student_id')

        #playground_reference = fields.Reference(comodel_name='academy.playground')

        #gate_many2onereference = fields.Many2onereference(comodel_name='academy.gate')

        birth_date = fields.Datetime()

        current_date = fields.Datetime(compute='_get_current_date')

        age = fields.Integer(compute='_compute_student_age')#Every time when we обращаемся to field - it compute on backand

        # self.flush()#remove all from cache
        # self.recompute()#every compute fields recompute again

        def _get_current_date(self):
            self.current_date = datetime.today()

        @api.depends('birth_date', 'current_date') #for compute function. current_date use compute too
        def _compute_student_age(self):
            if self.birth_date:
                self.age = self.current_date - self.birth_date
            else:
                self.age = 0 #If user not have birth_date

        def assign_teacher(self):
            #[1, 12, 14]
            self.teacher_ids = [(0, 0, {'name': 'Teacher A', 'student_id': self.id})] #(0, 0, values) - add a newly created record (15)
            #[1, 12, 14, 15]
            self.teacher_ids = [(1, 14, {'name': 'Teacher B', 'student_id': self.id})] #(1, id, values)  Rename teacherA(id 14) to teacherB. If no id 14 - Exceptiopn
            #[1, 12, 14, 15]
            self.teacher_ids = [(2, 12, 0)] #(2, id, 0) Remove 12 and delete it
            #[1, 14, 15]
            self.teacher_ids = [(3, 1, 0)] #(3, id, 0) Remove 10 from list without deleting on DB
            #[14, 15]
            self.teacher_ids = [(4, 1, 0)] #(4, id, 0) Add existing record. Add teacher 1 to the list
            #[1, 14, 15]
            self.teacher_ids = [(5, 0, 0)] #(5, 0, 0) Remove all record from list
            #[]
            self.teacher_ids = [(4, 17, 0)]
            #[17]
            self.teacher_ids = [(6, 0, [1, 14])] #(6, 0, ids) Replace record with new ones
            #[1, 14]

    class Teacher(models.Model):
        _name = 'academy.teacher'

        student_id = fields.Many2one(comodel_name='academy.student')

    class Attendee(models.Model):
        _name = 'academy.attendee'
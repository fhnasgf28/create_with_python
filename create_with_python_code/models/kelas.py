from odoo import models, fields


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string='Class Name', required=True)
    capacity = fields.Integer(string='Capacity', required=True)
    teacher_id = fields.Many2one('hr.employee', string='Class Teacher')
    student_ids = fields.One2many('school.student', 'class_id', string='Students')
    code = fields.Char(string='Class Code', required=True)
    description = fields.Text(string='Description')
    schedule = fields.Char(string='Schedule')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    active = fields.Boolean(string='Active', default=True)

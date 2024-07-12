from odoo import models, fields


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Student Name', required=True)
    age = fields.Integer(string='Age', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', required=True)
    class_id = fields.Many2one('school.class', string='Class')
    student_code = fields.Char(string='Student Code', required=True)
    birth_date = fields.Date(string='Birth Date')
    address = fields.Text(string='Address')
    parent_name = fields.Char(string='Parent Name')
    contact_number = fields.Char(string='Contact Number')
    admission_date = fields.Date(string='Admission Date', default=fields.Date.today)
    active = fields.Boolean(string='Active', default=True)
    photo = fields.Binary(string='Photo')

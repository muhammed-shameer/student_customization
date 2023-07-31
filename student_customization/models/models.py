
from odoo import models, fields, api


class StudentCustomization(models.Model):
    _name = 'student.customization'
    _description = 'Student Customization'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    classes = fields.Char(string="Class")

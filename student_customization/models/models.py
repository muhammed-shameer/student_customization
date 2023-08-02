from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date


class StudentCustomization(models.Model):
    _name = 'student.customization'
    _description = 'Student Customization'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age", compute="_compute_birthday", store=True)
    dob = fields.Date(string="Date Of Birth")
    birth = fields.Char(string="Birthday", compute="_compute_birthday", store=True)
    classes = fields.Char(string="Class")

    @api.depends('dob')
    def _compute_birthday(self):
        for record in self:
            if record.dob:
                delta = relativedelta(date.today(), record.dob)
                record.age = delta.years
                today = date.today()
                next_birthday = date(today.year, record.dob.month, record.dob.day)
                if next_birthday < today:
                    next_birthday = next_birthday + relativedelta(years=1)
                days_left = (next_birthday - today).days
                if days_left == 0:
                    record.birth = 'Today is birthday'
                else:
                    record.birth = f'{days_left} days left for birthday'
            else:
                record.birth = ''

# @api.depends('dob')
# def _compute_birthday(self):
#     for record in self:
#         if record.dob and record.dob.month == date.today().month and record.dob.day == date.today().day:
#             record.birth = 'Today is birthday'
#         else:
#             record.birth = ''

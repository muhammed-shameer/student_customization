# -*- coding: utf-8 -*-
# from odoo import http


# class StudentCustomization(http.Controller):
#     @http.route('/student_customization/student_customization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_customization/student_customization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_customization.listing', {
#             'root': '/student_customization/student_customization',
#             'objects': http.request.env['student_customization.student_customization'].search([]),
#         })

#     @http.route('/student_customization/student_customization/objects/<model("student_customization.student_customization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_customization.object', {
#             'object': obj
#         })

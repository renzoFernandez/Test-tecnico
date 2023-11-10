# -*- coding: utf-8 -*-
# from odoo import http


# class Facultad(http.Controller):
#     @http.route('/facultad/facultad', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/facultad/facultad/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('facultad.listing', {
#             'root': '/facultad/facultad',
#             'objects': http.request.env['facultad.facultad'].search([]),
#         })

#     @http.route('/facultad/facultad/objects/<model("facultad.facultad"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('facultad.object', {
#             'object': obj
#         })

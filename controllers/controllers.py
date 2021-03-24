# -*- coding: utf-8 -*-
from odoo import http

# class Bibliotheque(http.Controller):
#     @http.route('/bibliotheque/bibliotheque/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bibliotheque/bibliotheque/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bibliotheque.listing', {
#             'root': '/bibliotheque/bibliotheque',
#             'objects': http.request.env['bibliotheque.bibliotheque'].search([]),
#         })

#     @http.route('/bibliotheque/bibliotheque/objects/<model("bibliotheque.bibliotheque"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bibliotheque.object', {
#             'object': obj
#         })
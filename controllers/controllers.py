# -*- coding: utf-8 -*-
from odoo import http

# class BibliothequeCheckout(http.Controller):
#     @http.route('/bibliotheque_checkout/bibliotheque_checkout/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bibliotheque_checkout/bibliotheque_checkout/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bibliotheque_checkout.listing', {
#             'root': '/bibliotheque_checkout/bibliotheque_checkout',
#             'objects': http.request.env['bibliotheque_checkout.bibliotheque_checkout'].search([]),
#         })

#     @http.route('/bibliotheque_checkout/bibliotheque_checkout/objects/<model("bibliotheque_checkout.bibliotheque_checkout"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bibliotheque_checkout.object', {
#             'object': obj
#         })
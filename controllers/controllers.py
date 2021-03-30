# -*- coding: utf-8 -*-
from odoo import fields, http


class books(http.Controller):
 

    @http.route('/library/books' , auth='public')
    def list(self, **kw):
    	book = http.request.env['bibliotheque.book']
    	books = book.search([])
        return http.request.render("bibliotheque.listing", {'books': books})

   
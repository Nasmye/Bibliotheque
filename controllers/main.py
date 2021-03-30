from odoo import http
from odoo.addons.bibliotheque.controllers.controllers import books

class bookextended(books):
	@http.route()
	def list(self, **kwargs):
		response = super().list(**kwargs)
		if kwargs.get('available'):
			book = http.request.env['bibliotheque.book']
			books = book.search([('is_available', '=', True)])
			response.qcontext['books'] = books
		return response	
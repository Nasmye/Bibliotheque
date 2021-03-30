from odoo import api, fields, models

class Partner(models.Model):
	_inherit ='res.partner'
	
	published_book_ids = fields.One2many(
		'bibliotheque.book',
		'publisher_id',
		string='Published Books')
	book_ids = fields.Many2many(
		'bibliotheque.book', string='Authored Books')
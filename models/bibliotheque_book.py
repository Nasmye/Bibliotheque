from odoo import api, fields, models 
from odoo.exceptions import Warning

class book(models.Model):
	_name = 'bibliotheque.book'
	_description ='Book'

	name = fields.Char('Title', required=True)
	isbn = fields.Char('ISBN')
	active = fields.Boolean('Active ?', default=True)
	date_published = fields.Date()
	image = fields.Binary('Cover')
	publisher_id = fields.Many2one('res.partner', string='Publisher')
	author_ids = fields.Many2many('res.partner', string='Authors')


	@api.multi
	def _check_isbn(self):
		self.ensure_one()
		digits=  [int(x) for x in self.isbn if x.isdigit()]
		if len(digits) == 13:
			ponderations = [1, 3]*6
			total = sum(a * b for a, b in zip(digits[:12], ponderations))
			remain = total % 10
			check = 10 -remain if remain !=0 else 0
			return digits[-1] ==check 

	@api.multi
	def button_check_isbn(self):
		for book in self:
			if not book.isbn:
				raise Warning('Please provide a ISBN %s' %book.name)
			if book.isbn and not book._check_isbn():
				raise Warning('%s is an invalid ISBN' %book.isbn)	
		return True	

	@api.multi
	def is_available(self):
		return True

				

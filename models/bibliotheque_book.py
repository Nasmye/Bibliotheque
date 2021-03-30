from odoo import api, fields, models 
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError
import logging 

class book(models.Model):
	_name = 'bibliotheque.book'
	_description ='Book'

	name = fields.Char('Title',help='Book Cover Title', required=True)
	isbn = fields.Char('ISBN')
	active = fields.Boolean('Active ?', default=True)
	date_published = fields.Date()
	image = fields.Binary('Cover')
	publisher_id = fields.Many2one('res.partner', string='Publisher')
	author_ids = fields.Many2many('res.partner', string='Authors')

	book_type = fields.Selection ([('paper','Paperback'),
								   ('hard','Hardcover'),
								   ('electronic','Electronic'),
								   ('other','Other')],
								   'Type')
	note = fields.Text('Internal Notes')
	descr = fields.Html('Description')

	copies = fields.Integer(default=1)
	avg_rating = fields.Float('Average Rating', (3,2))


	price = fields.Monetary('Price', 'currency_id')
	currency_id = fields.Many2one('res.currency')

	
	# #=lamda self: fields.Datetime.now()    ---> is the same as:
	# #=_default_last_borrow_date  /// def _default_last....(self):  return fields.Datetime.now()

	last_borrow_date = fields.Datetime('Last Borrowed On',
										default=lambda self: fields.Datetime.now())

	category_id = fields.Many2one('bibliotheque.book.category',string='Category')

	publisher_country_id = fields.Many2one(
		'res.country',
		string='Publisher Country',
		compute='_compute_publisher_country (related)',
		related='publisher_id.country_id',
		redonly=False,
		inverse='_inverse_publisher_country',
		search='_search_publisher_country',)
	

	_sql_constraints = [
	('bibliotheque_book_name_date_uq',  #Constaint unique identifier
		'UNIQUE (name,date_published)',  #Constraint SQL syntax
		'Book title and publication date must be unique.'), #KillMessage
	('bibliotheque_book_check_date',
		'CHECK (date_published <= current_date)',
		'Publication date must not be in the future.'),
	]
	
	# author_ids = fields.Many2many(
	# 	'res.partner',                       #related model
	# 	'bibliotheque_book_res_partner_rel', #relation table name
	# 	'a_id',                              #rel table field for "this" record
	# 	'p_id',                              #rel table field for "other" record
	# 	 string='Authors')


	@api.multi
	def _check_isbn(self):
		self.ensure_one()
		digits= [int(x) for x in self.isbn if x.isdigit()]
		digits = digits.replace('-','').replace(' ', '')
		logging.warn('\n {} \n'.format(digits))
		if len(digits) == 13:
		    product = (sum(int(ch) for ch in digits[::2]) 
		               + sum(int(ch) * 3 for ch in digits[1::2]))
		    logging.warn('\n {} \n'.format(product))
		    return product % 10 == 0

		# digits= [int(x) for x in self.isbn if x.isdigit()]
		# if len(digits) == 13:
		# 	ponderations = [1, 3]*6
		# 	total = sum(a * b for a, b in zip(digits[:12], ponderations))
		# 	remain = total % 10
		# 	check = 10 -remain if remain !=0 else 0
		# 	logging.warn('\n {} , {}\n '.format(digits[-1], check))
		# 	return digits[-1] == check 

		

		

		# digits = digits.replace('-','').replace(' ', '')
	    	

	@api.multi
	def button_check_isbn(self):
		for book in self:
			if not book.isbn:
				raise Warning('Please provide an ISBN for %s' %book.name)
			if book.isbn and not book._check_isbn():
				raise Warning('%s is an invalid ISBN' %book.isbn)	
			else:
				raise Warning('%s is a valid ISBN' %book.isbn)	
		return True	

	@api.multi
	def is_available(self):
		return True

	@api.depends('publisher_id.country_id')
	def _compute_publisher_country(self):
		for book in self:
			book.publisher_country_id = book.publisher_id.country_id


	@api.depends('publisher_country_id')
	def _inverse_publisher_country(self):
		for book in self:
			book.publisher_id.country_id = book.publisher_country_id	

	
	def _search_publisher_country(self, operator, value):
		return [('publisher_id.country_id',operator , value)]	

	@api.constrains('isbn')
	def _constain_isbn_valid(self):
		for book in self:
			if book.isbn and not book._check_isbn():
				raise ValidationError('%s is an invalid ISBN' %book.isbn)



				

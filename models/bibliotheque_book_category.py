from odoo import api, models, fields

class bookcategory(models.Model):
	_name = 'bibliotheque.book.category'
	_description = 'Book Category'
	_parent_store = True

	name = fields.Char(translate=True ,required=True)

	
	parent_id = fields.Many2one(
		'bibliotheque.book.category',
		string='Parent Category',
		ondelete='restrict')
	child_ids = fields.One2many(
		'bibliotheque.book.category',
		'parent_id',
		string='Subcategories')

	highlighted_id = fields.Reference(
		[('bibliotheque.book','Book'),
		('res.partner','Author')],
		'Category Highlight',)

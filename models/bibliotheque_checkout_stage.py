from odoo import fields , api, models 
 
class checkoutstage(models.Model):
	_name = 'bibliotheque.checkout.stage'  
	_desription = 'Checkout Stage'
	_order = 'sequence,name'

	name= fields.Char()
	sequence = fields.Integer(default=10)
	fold = fields.Boolean()
	active = fields.Boolean(default=True)
	state = fields.Selection(
		[('new','New'),
		('open','Borrowed'),
		('done','Returned'),
		('cancel','Cancelled')],
		default='new',)



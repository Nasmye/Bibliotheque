from odoo import fields, models ,api

class Member(models.Model):
	_name = 'bibliotheque.member'
	_description = 'Bibliotheque Member'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	card_number = fields.Char()
	partner_id = fields.Many2one(
		'res.partner',
		delegate=True,
		ondelete='cascade',
		required=True)
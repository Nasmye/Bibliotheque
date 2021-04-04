# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class checkout(models.Model):
    _name = 'bibliotheque.checkout'
    _description = 'Checkout Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    member_id = fields.Many2one(
    	'bibliotheque.member',
    	required=True)
    user_id = fields.Many2one(
    	'res.users',
    	'Bibliotheque',
    	default=lambda s: s.env.uid)
    request_date = fields.Date(
    	default=lambda s: fields.Date.today())
    line_ids= fields.One2many(
    	'bibliotheque.checkout.line',
    	'checkout_id',
    	string='Borrowed Books',)

    @api.model
    def _default_stage(self):
        stage = self.env['bibliotheque.checkout.stage']
        return stage.search([], limit=1)

    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([],order=order)  

    stage_id = fields.Many2one(
        'bibliotheque.checkout.stage',
        default=_default_stage,
        group_expand='_group_expand_stage_id')
    state = fields.Selection(related='stage_id.state')  

    @api.onchange('member_id')
    def onchange_member_id(self):
        today = fields.Date.today()
        if self.request_date != today:
            self.request_date = fields.Date.today()
            return {
            'warning': {
                'title' : 'changed request date',
                'message' : 'request date changed tpt tpday',
                }
            }

    checkout_date = fields.Date(readonly=True)
    close_date = fields.Date(readonly=True)        

    @api.multi
    def write(self, vals):
        if 'stage_id' in vals:
            stage = self.env['bibliotheque.checkout.stage']
            new_state = stage.browse(vals['stage_id']).state
            if new_state == 'open' and self.state != 'open':
                vals['checkout_date'] = fields.Date.today()
            if new_state == 'done' and self.state != 'done':
                vals['close_date'] = fields.Date.today()

        super().write(vals)
        return True  

  

    @api.model
    def create(self, vals):
        if 'stage_id' in vals:
            stage = self.env['bibliotheque.checkout.stage']
            new_state = stage.browse(vals['stage_id']).state
            if new_state == 'open':
                vals['checkout_date'] = fields.Date.today()
            new_record = super().create(vals)
            if new_record.state == 'done':
                raise exceptions.UserError(
                    'Not allowed to create a checkout in the done state.')
            return new_record

    def button_done(self):
        stage = self.env['bibliotheque.checkout.stage']
        done_stage = stage.search(
            [('state', '=', 'done')],
            limit=1)
        for checkout in self:
            checkout.stage_id = done_stage
        return True 



class CheckoutLine(models.Model):
	_name = 'bibliotheque.checkout.line'
	_description = 'Borrow Request Line'


	checkout_id = fields.Many2one('bibliotheque.checkout.stage')
	book_id = fields.Many2one('bibliotheque.book')



from odoo import fields, models, api

class AbstractOffer(models.AbstractModel):
    _name = 'abstract.model.offer'
    _description = 'Abstract Offers'

    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer', required=True)
    partner_email = fields.Char(related='partner_id.email', string='Email')
    partner_phone = fields.Char(related='partner_id.phone', string='Phone')
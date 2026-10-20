from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class AbstractOffer(models.AbstractModel):
    _name = 'abstract.model.offer'
    _description = 'Abstract Offers'

    partner_email = fields.Char(string='Email')
    partner_phone = fields.Char(string='Phone')

class TransientOffer(models.TransientModel):
    _name = 'transient.model.offer'
    _description = 'Transient Offers'

class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property Offers'

    name = fields.Char(string='Description', compute='_compute_name')
    price = fields.Float(string='Price', required=True)
    status = fields.Selection(selection=[
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    property_id = fields.Many2one(comodel_name='estate.property', string='Property')
    validity = fields.Integer(string='Validity (days)')
    deadline = fields.Date(string='Deadline', compute='_compute_deadline')
    creation_date = fields.Date(string='Creation Date')

    @api.depends('validity', 'creation_date')
    def _compute_deadline(self):
        for record in self:
            if not record.validity or not record.creation_date:
                record.write({
                    'deadline': False
                })
            else:
                record.write({
                    'deadline': record.creation_date + relativedelta(days=record.validity)
                })
    
    @api.constrains('validity')
    def _check_validity(self):
        for record in self:
            if record.validity < 1:
                raise ValidationError(_('Validity field must be greater than 1'))

    @api.depends('property_id','partner_id')
    def _compute_name(self):
        for record in self:
            if record.property_id and record.partner_id:
                record.name = f"{record.property_id.name} - {record.partner_id.name}"
            else:
                record.name = False

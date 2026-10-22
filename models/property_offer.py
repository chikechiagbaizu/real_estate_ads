from odoo import _, api, fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError, UserError

class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property Offers'
    _inherit = ['abstract.model.offer']

    name = fields.Char(string='Description', compute='_compute_name')
    price = fields.Float(string='Price', required=True)
    status = fields.Selection(selection=[
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status', readonly=True)
    property_id = fields.Many2one(comodel_name='estate.property', string='Property', required=True)
    validity = fields.Integer(string='Validity (days)', default=7)
    deadline = fields.Date(string='Deadline', compute='_compute_deadline')
    creation_date = fields.Date(string='Creation Date', default=fields.Date.today, readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            property_id = vals.get('property_id')
            if property_id:
                property = self.env['estate.property'].browse(property_id)
                if property.state == 'accepted':
                    raise UserError(-('You cannot add an offer to a %s property.',property.state))
        offers = super().create(vals_list)
        for property in offers.property_id:
            if property.state == 'new':
                property.state = 'received'
        return offers
    
    @api.depends('validity', 'creation_date')
    def _compute_deadline(self):
        for record in self:
            if record.creation_date:
                record.deadline = record.creation_date + relativedelta(days=record.validity)
            else:
                record.deadline = False
    
    @api.constrains('validity')
    def _check_validity(self):
        for record in self:
            if record.validity < 1:
                raise ValidationError(_('Validity field must be greater than 0'))

    @api.depends('property_id','partner_id')
    def _compute_name(self):
        for record in self:
            if record.property_id and record.partner_id:
                record.name = f"{record.property_id.name} - {record.partner_id.name}"
            else:
                record.name = False

    def action_accept_offer(self):
        self.ensure_one()
        if self.property_id.offer_ids.filtered(lambda o: o.status == 'accepted'):
            raise UserError(_('An offer has already been accepted for this property.'))
        self.status = 'accepted'
        self.property_id.state = 'accepted'
        
    def action_decline_offer(self):
        self.ensure_one()
        if self.status == 'refused':
            raise UserError('Property offer already refused.')
        self.status = 'refused'
        self.property_id.state = 'received'

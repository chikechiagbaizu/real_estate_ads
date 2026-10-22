from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

class Property(models.Model):
    _name = 'estate.property'
    _description = 'Properties'

    name = fields.Char(string='Name', required=True)
    tag_ids = fields.Many2many(comodel_name='estate.property.tag', string='Property Tag')
    type_id = fields.Many2one(comodel_name='estate.property.type', string='Property Type')
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price', compute='_compute_selling_price', store=True)
    best_offer = fields.Float(string='Best Offer', compute='_compute_best_offer')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Fascades')
    garage = fields.Boolean(string='Garage', default=False)
    garden = fields.Boolean(string='Garden', default=False)
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(selection=[
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ],string='Garden Orientation', default='north')
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_id', string='Offers')
    sales_id = fields.Many2one(comodel_name='res.users', string='Sales Representative')
    buyer_id = fields.Many2one(comodel_name='res.partner', string='Buyer', domain=[('is_company','=',False)])
    phone = fields.Char(related='buyer_id.phone', string='Phone')
    total_area = fields.Integer(compute='_compute_total_area', string='Total Area (sqm)')
    state = fields.Selection(selection=[
        ('new','New'),
        ('received','Offer Received'),
        ('accepted','Offer Accepted'),
        ('sold','Sold'),
        ('cancelled','Cancelled'),
    ], default='new', string='Status')

    offer_count = fields.Integer(string='Offer Count', compute='_compute_offer_count')

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    def action_sold(self):
        if self.state == 'cancelled':
            raise UserError(_('Cannot be sold. Property state is %s.', self.state))
        elif self.state == 'sold':
            raise UserError(_('Property is already %s.', self.state))
        else:
            self.state = 'sold'
    
    def action_cancel(self):
        if self.state == 'sold':
            raise UserError(_('Cannot cancel a sold property.'))
        elif self.state == 'cancelled':
            raise UserError(_('Property state has already been cancelled.'))
        else:
            self.state = 'cancelled'

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
    
    def action_view_offers(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Property Offers',
            'res_model': 'estate.property.offer',
            'view_mode': 'list,form',
            'domain':[('property_id','=',self.id)],
            'context':{
                'default_property_id': self.id,
            }
        }
    
    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < 0.0:
                raise ValidationError('Selling price cannot be negative.')

    @api.constrains('expected_price')
    def _check_expected_price(self):
        for record in self:
            if record.expected_price < 0.0:
                raise ValidationError('Expected price cannot be negative.')

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            if record.offer_ids:
                record.best_offer = max(record.offer_ids.mapped('price'))
            else:
                record.best_offer = 0
    
    @api.depends('offer_ids.status','offer_ids.price')
    def _compute_selling_price(self):
        for record in self:
            accepted = record.offer_ids.filtered(lambda o: o.status == 'accepted')
            if accepted:
                record.selling_price = record.best_offer
            else:
                record.selling_price = 0.0
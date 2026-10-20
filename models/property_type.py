from odoo import fields, models

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'

    name = fields.Char(string='Name', required=True)
    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='type_id', string='Properties')
from odoo import fields, models

class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Property Tag'

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string="Color Index", default=0)
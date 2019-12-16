from openerp import models, fields, api

class det(models.Model):
    _name = 'relac.det'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()
    enc         = fields.Many2one('relac.enc')
    #relacs       = fields.One2many('relacs.relac', 'area')

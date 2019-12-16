from openerp import models, fields, api

class enc(models.Model):
    _name = 'relac.enc'

    name        = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()
    det         = fields.One2many('relac.det','enc')

#    area        = fields.Many2one('relacs.area')
#    gerencia    = fields.Many2one('relacs.gerencia')
#    unidad      = fields.Many2one('relacs.unidad')
#    depto       = fields.Many2one('relacs.depto')
#    relaceso     = fields.Many2one('relacs.relaceso')
#    fecha       = fields.Char()
#    pasos       = fields.Many2many('relacs.paso')

#    @api.onchange('area')
#    def _onchange_area(self):
#        if not self.name:
#            self.name = self.area.name

#    @api.onchange('gerencia')
#    def _onchange_gerencia(self):
#        if not self.name:
#            self.name = self.gerencia.name

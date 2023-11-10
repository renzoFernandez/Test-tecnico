from odoo import api, fields, models



class programa(models.Model):
    _name='facultad.programa'
    _description = 'Permite definir las caracteristicas del programa'

    nombre = fields.Char()
    descripcion = fields.Text()

    inscripcion_ids = fields.One2many('facultad.inscripcion','programa_id',string='inscripciones')
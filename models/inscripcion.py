from odoo import api, fields, models


class inscripcion(models.Model):
    _name='facultad.inscripcion'

    alumno_id = fields.Many2one('facultad.alumno',string='alumno')
    programa_id = fields.Many2one('facultad.programa',string='programa')
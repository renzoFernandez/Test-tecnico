# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class facultad(models.Model):
#     _name = 'facultad.facultad'
#     _description = 'facultad.facultad'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models,fields, api

class alumno(models.Model):
    _name = 'facultad.alumno'
    _description = 'Permite definir la persona que se va inscribir en algun programa'

    nombre = fields.Char()
    apellido = fields.Char()
    legajo = fields.Integer()
    fecha_nacimiento = fields.Date()
    email = fields.Char()
    telefono = fields.Integer()


    inscripcion_ids = fields.One2many('facultad.inscripcion','alumno_id',string='inscripciones')

class programa(models.Model):
    _name='facultad.programa'
    _description = 'Permite definir las caracteristicas del programa'

    nombre = fields.Char()
    descripcion = fields.Text()

    inscripcion_ids = fields.One2many('facultad.inscripcion','programa_id',string='inscripciones')
class inscripcion(models.Model):
    _name='facultad.inscripcion'

    alumno_id = fields.Many2one('facultad.alumno',string='alumno')
    programa_id = fields.Many2one('facultad.programa',string='programa')
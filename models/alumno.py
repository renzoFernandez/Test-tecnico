from odoo import api, fields, models

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
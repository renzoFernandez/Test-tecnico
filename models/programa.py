from odoo import api, fields, models
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class programa(models.Model):
    _name='facultad.programa'
    _description = 'Permite definir las caracteristicas del programa'
     
    nombre = fields.Char()
    descripcion = fields.Text()

    inscripcion_ids = fields.One2many('facultad.inscripcion','programa_id',string='inscripciones')

    def action_test(self):
        for record in self:
            alumnos = []
            alumnos_id = []
            for ins in record.inscripcion_ids:
                '''self.env.cr.execute('SELECT * FROM facultad_alumno')
                result = list(line[0] for line in self.env.cr.fetchall())'''
                alumnos_id .append(ins.alumno_id.id)
                alumno = {
                    "nombre" : ins.alumno_id.nombre,
                    "apellido":ins.alumno_id.apellido,
                    "legajo":ins.alumno_id.legajo,
                    "fecha_nacimiento" : ins.alumno_id.fecha_nacimiento,
                    "email":ins.alumno_id.email,
                    "telefono":ins.alumno_id.telefono
                }
                alumnos.append(alumno)
        _logger.info(alumnos)
        return{
            'type':'ir.actions.act_window',
            'name' : 'ALUMNOS',
            'view_type': 'form',
            'view_mode': 'tree,pivot',
            'res_model' : 'facultad.alumno',
            'domain': [('id','in',alumnos_id)]
        }
                
            
            
        
        
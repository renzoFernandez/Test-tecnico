# -*- coding: utf-8 -*-
{
    'name': "Facultad",

    'summary': """
        Test tecnico-ADEN""",

    'description': """
        Test tecnico-ADEN para el puesto de desarrollador backend
    """,

    'author': "Renzo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/alumno_views.xml',
        'views/programa_views.xml',
        'views/inscripcion_views.xml',
        'views/menu_item_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}

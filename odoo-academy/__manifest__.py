# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',
    'version': '0.24',
    'description': """Academy module for manage Training: Courses, Sessions...""",
    'category': 'Training',
    'author': 'NVP',

    'depends': ['base'],
    'data': [
        #data
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/menu.xml'
        #views
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
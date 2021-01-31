# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',
    'version': '0.23',
    'description': """Academy module for manage Training: Courses, Sessions...""",
    'category': 'Training',
    'author': 'NVP',

    'depends': ['base'],
    'data': [
        #data
        'views/menu.xml'

        #'security/ir.model.access.csv'
        #views
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
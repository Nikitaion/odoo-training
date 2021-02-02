# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',
    'version': '0.25',
    'description': """Academy module for manage Training: Courses, Sessions...""",
    'category': 'Training',
    'author': 'NVP',

    'depends': ['base'],
    'data': [
        #data
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/menu.xml',
        'views/attendee_view.xml',
        'views/inherit_test'

        #views
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',
    'version': '1.4',
    'description': """Academy module for manage Training: Courses, Sessions...""",
    'category': 'Training',
    'author': 'NVP',

    'depends': ['base', 'portal'],
    'data': [
        #data
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/menu.xml',
        'views/attendee_view.xml',
        'views/inherit_test.xml',
        'views/session_view.xml',
        'views/wizard_for_update_course_name.xml',
        'views/report.xml',
        'views/qweb_template_for_controller.xml'

        #views
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# -*- coding: utf-8 -*-
{
    'name': "Timesheet Add-On",

    'summary': """Allows to print timesheets""",

    'description': """This module allows timesheets printing related to an employee""",

    'author': "AtomX System",

    'website': "http://atomxsystem.eu",

    'category': 'Tools',

    'version': '0.1.4',

    # any module necessary for this one to work correctly
    'depends': ['timesheet_grid', 'hr'],

    # always loaded
    'data': [
        'views/templates.xml',
        'views/report.xml',
    ],
    'installable': True,
    'auto_install': False,
}
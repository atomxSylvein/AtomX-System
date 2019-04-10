# -*- coding: utf-8 -*-
{
    'name': "Timesheet Add-On",

    'summary': """Allows to print timesheets""",

    'description': """This module allows timesheets printing related to an employee""",

    'author': "AtomX System",

    'website': "http://atomxsystem.eu",

    'category': 'Tools',

    'version': '0.2.42',

    # any module necessary for this one to work correctly
    'depends': ['timesheet_grid', 'hr'],

    # always loaded
    'data': [
        'views/templates.xml',
        'reports/timesheet_report.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
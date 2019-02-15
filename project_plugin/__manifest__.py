# -*- coding: utf-8 -*-
{
    'name': "Project Plugin",

    'summary': """Add fields to project module""",

    'description': """This module adds some fields to the Project module""",

    'author': "AtomX System",

    'website': "http://atomxsystem.eu",

    'category': 'Tools',

    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
}
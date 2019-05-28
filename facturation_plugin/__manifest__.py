# -*- coding: utf-8 -*-
{
    'name': "Invoicing Plugin",

    'summary': """Add fields to invoicing module""",

    'description': """This module modify invoices generated by Invoicing module""",

    'author': "AtomX System",

    'website': "http://atomxsystem.eu",

    'category': 'Tools',

    'version': '1.9',

    # any module necessary for this one to work correctly
    'depends': ['account', 'sale'],

    # always loaded
    'data': [
        'views/templates.xml',
        'report/external_layout.xml',
        'report/invoices_documents.xml',
    ],
    'installable': True,
    'auto_install': False,
}
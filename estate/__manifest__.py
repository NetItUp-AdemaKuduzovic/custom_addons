# -*- coding: utf-8 -*-
{
    'name': "Real Estate Tutorial",

    # any module necessary for this one to work correctly
    'depends': ['base'], 

    'data': [
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
        
    ],

    'license': 'OPL-1', 
    'installable': True, 
    'application': True
}


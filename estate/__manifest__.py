# -*- coding: utf-8 -*-
{
    'name': "Real Estate Tutorial",

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'], 

    'demo': [
        'demo/demo.xml',
    ],

    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',
        'views/res_users_views.xml',
    ],

    'license': 'OPL-1', 
    'installable': True, 
    'application': True
}


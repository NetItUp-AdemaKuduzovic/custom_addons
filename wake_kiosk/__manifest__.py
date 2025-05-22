# -*- coding: utf-8 -*-
{
    'name': "wake_kiosk",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_attendance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    
    ],
    
    'assets': {
        'hr_attendance.assets_public_attendance': [
            'wake_kiosk/static/src/public_kiosk/public_kiosk_app.js'
        ],
    },

    'license': 'OPL-1', 
    'installable': True,
}


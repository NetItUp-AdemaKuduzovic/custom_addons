# -*- coding: utf-8 -*-
{
    'name': "Send info email",

    'summary': "Send informative emails to employees about their attendance activity",

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
    'depends': ['base','hr', 'hr_attendance', 'mail'], 

    # always loaded
    'data': [
        'views/mail_templates.xml',
        # 'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
    
    ],
    'license': 'OPL-1',
    'installable': True,
}


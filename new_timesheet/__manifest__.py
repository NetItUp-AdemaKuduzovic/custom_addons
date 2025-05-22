# -*- coding: utf-8 -*-
{
    'name': "new timesheet",

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
    'depends': ['base', 'analytic', 'hr_timesheet','helpdesk_timesheet'],

    # always loaded
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/hr_timesheet_activity_views.xml',
        'views/hr_timesheet_service_views.xml',
        'views/hr_timesheet_menus.xml',
        'views/hr_timesheet_views.xml',
        'views/helpdesk_ticket_views.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
    ],
    'license': 'OPL-1',
    'installable': True,
}


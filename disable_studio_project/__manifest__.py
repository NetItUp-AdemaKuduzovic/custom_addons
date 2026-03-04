# -*- coding: utf-8 -*-
{
    "name": "Disable Studio Features",
    "summary": "",
    "description": """
    Disable studio button from systray add 'Add custom Field' from list views
    """,
    "license": "OPL-1",
    "author": "Adema Sarajlija",
    "website": "",
    "category": "Customization",
    "version": "18.0.0.0",
    "installable": True,
    "application": True,
    "depends": [
        "base",
        "web", 
        "web_studio"
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/niu_timestamp_views.xml'
    ],
    "assets": {
        'web.assets_backend': [
        ],
    },
}
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
        "web_studio",
    ],
    "data": [
    ],
    "assets": {
        'web.assets_backend': [
            'disable_studio_project/static/src/systray_item/systray_item.js',
            'disable_studio_project/static/src/systray_item/views/list/list_renderer_desktop.js'
        ],
    },
}
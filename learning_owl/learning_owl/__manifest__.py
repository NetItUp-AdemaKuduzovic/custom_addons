{
    'name': "Learning Owl",
    'version': '18.0.1.0.0',
    'depends': ['sale', 'stock', 'mrp'],
    'author': "ASK",
    'category': 'Category',
    'description': """
    Module to learn Owl templates in Odoo.
    """,
    'data': [
        'views/sale_order_views.xml',
    ],
    "assets": {
        "web.assets_backend": [
            # "learning_owl/static/src/components/**/*",
            # "learning_owl/static/src/lib/**/*",
            
        ]
    }
}
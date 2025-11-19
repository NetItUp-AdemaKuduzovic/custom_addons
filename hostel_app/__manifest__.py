{
    'name': "Hostel Management",
    'summary': "Manage Hostel easily",
    'description': """Efficiently manage the entire residential 
        facility in the school.""", 
    'author': "Adema Sarajlija",
    'website': "",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'data/data.xml',
        'security/hostel_security.xml',
        'security/ir.model.access.csv',
        'views/hostel_room_views.xml',
        'views/hostel_student_views.xml',
        'views/hostel_amenities_views.xml',
        'views/hostel_categ_views.xml',
        'views/hostel_hostel_views.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'web/static/src/xml/**/*',
    #     ],
    # },
    # 'demo': ['demo.xml'],
}
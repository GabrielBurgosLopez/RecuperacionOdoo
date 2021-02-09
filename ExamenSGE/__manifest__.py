# -*- coding: utf-8 -*-
{
    'name': "Natural Park",

    'summary': """Manage Natural Parks""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Gabriel Burgos",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # debo añadir la referncia a baseModule
    'depends': ['base','baseModule'],
    
    # always loaded
    'data': [
        'views/naturalPark.xml'
    ],
   
}
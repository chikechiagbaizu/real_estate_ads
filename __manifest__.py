{
    'name': 'Real Estate Ads',
    'summary': 'Real Estate Ads',
    'description': """
    Odoo technical course project developed while following
    Miracle Ayodele's Odoo 16/17 technical course, adapted
    for Odoo 19.0.
    """,
    'author': 'Chike Chiagbaizu',
    'maintainer': 'Chike Chiagbaizu',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'sequence': 20,
    'category': 'Sales',
    'application': True,
    'installable': True,
    'depends': [
        'base',
    ],
    'data': [
        # Security & Data
        'security/ir.model.access.csv',
        'data/estate_property_type.xml',
        'data/estate.property.tag.csv',

        # Views
        'views/property_view.xml',
        'views/property_offer_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',

        # Actions
        'views/property_action.xml',
        'views/property_offer_action.xml',
        'views/property_type_action.xml',
        'views/property_tag_action.xml',

        # Menus
        'views/menu_items.xml',
    ],

    # 'demo': [
    #     'demo/estate_property_tag.xml',
    #     'demo/estate_property_type.xml'
    # ]
}
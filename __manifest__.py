{
    'name': 'Library Management',
    'description': 'Manage library book catalogue and lending.',
    'author': 'Federico Gregori',
    'website': 'https://github.com/FedericoGregori',
    'category': 'Library',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/res_partner_view.xml',
        'views/book_list_template.xml'
    ],
    'demo': [
        'data/res.partner.csv',
        'data/library.book.csv',
        'data/book_demo.xml'
    ],
}

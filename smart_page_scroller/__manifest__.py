# -*- encoding: utf-8 -*-
{
    'name': 'smart page scroller',
    'summary': 'product page in scroll button apply',
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'depends': ['website_sale',
                'website', 'product',
                'sale'
                ],
    'category': 'Website',
    'version': '10.0.1.0.0',
    'description': """
    -- in website product page scroll top buttton apply.
    """,
    'data': [
        'view/assets_inherit.xml',
        'view/websit_sale_inherit_template.xml',
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'auto_install': False,
    'installable': True,
    'application': False
}

#  -*- coding: utf-8 -*-
# Part of AktivSoftware See LICENSE file for full
# copyright and licensing details.
{
    'name': 'smart page scroller',
    'summary': 'product page in scroll button apply',
    'author': "Aktiv Software",
    'website': "http://alhamdanconsulting.com/",
    'depends': ['website_sale',
                'sale_management',
                'website', 'product'
                ],
    'category': 'Website',
    'version': '11.0.1.0.0',
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

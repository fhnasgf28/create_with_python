# -*- coding: utf-8 -*-
{
    'name': "Python Code",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'stock', 'purchase','hr_attendance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/kelas_views.xml',
        'views/siswa_views.xml',
    ],
    'installable': True,
    'application': True,
}

# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Todo Projects",
    "version": "10.0.1.0.0",
    "author": "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Project",
    "summary": "All the projects I need to do",
    "depends": [
        'project',
    ],
    "data": [
        # 'data/todo_data.xml',
        'data/server_actions.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizards/todo_stats_view.xml',
    ],
    "qweb": [
    ],
    "test": [
    ],
    "images": [
    ],
    "pre_init_hook": False,
    "post_init_hook": False,
    "uninstall_hook": False,
    "auto_install": False,
    "installable": True,
    "application": False,
    "external_dependencies": {
        'python': [],
    },
}

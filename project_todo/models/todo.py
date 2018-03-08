# -*- coding: utf-8 -*-
# © 2018 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class Todo(models.Model):
    _name = 'todo'
    _description = 'Todo Model'


    todo_text = fields.Text('Text todo')
    user = fields.Many2One('res.users', required=True)


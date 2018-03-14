# -*- coding: utf-8 -*-
# © 2018 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class ProjectTodo(models.Model):
    _name = 'diary.item'
    _description = 'Diary Item'

    name = fields.Char()
    date = fields.Datetime()
    content = fields.Text()


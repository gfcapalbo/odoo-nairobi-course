# -*- coding: utf-8 -*-
# © 2018 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models
import datetime

class ProjectTodo(models.Model):
    _name = 'project.todo'
    _description = 'Todo Model'

    name = fields.Char()
    text_todo = fields.Text('Content of Todo')
    deadline = fields.Datetime(required=True , default=fields.Date.today())
    days_left = fields.Integer(
    )
    is_urgent = fields.Boolean()


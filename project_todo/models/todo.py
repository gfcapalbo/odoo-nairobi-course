# -*- coding: utf-8 -*-
# © 2018 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class ProjectTodo(models.Model):
    _name = 'project.todo'
    _description = 'Todo Model'

    name = fields.Char()
    text_todo = fields.Text('Content of Todo')
    user = fields.Many2one('res.users', required=True)
    todo_type = fields.Many2one(
        string='type Of Todo', 

        comodel_name='project.todo.type')
    done = fields.Boolean(default=False)

    def do_todo(self):
        self.write({'done': True})


    @api.multi
    def server_action_was_here(self):
        for this in self:
            this.write(
                {'text_todo': this.text_todo + 'A server Action Was here'})


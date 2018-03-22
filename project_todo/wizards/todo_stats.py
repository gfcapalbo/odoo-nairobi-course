# -*- coding: utf-8 -*-

import datetime
from odoo import api, models, fields



# wizard that given date and user, calculates the stats for that user

# how many done 
# how many created by him
# how many created that where given to him
# How many modified by him



class ProjectTodoStats(models.TransientModel):
    
    _name = "project.todo.stats"
    _description = " statistics for project todo"

    user_id = fields.Many2one('res.users', string='Stats Of')
    from_date = fields.Date(string='After Date')


    def launch_stats(self):
        """
        functions can return actions, it's a valid alternative 
        to using menues to launch actions. and can be used to implement 
        multi popup types of situations (your context will follow you around)
        """
        import pudb
        pudb.set_trace()
        return {
                'type': 'ir.actions.act_window',
                'res_model':  'project.todo',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                "view_id": self.env.ref('project_todo.form_todos'),
                "views": [(self.env.ref('project_todo.form_todos'), 'form')]
        }


    """ Another inheritance example
    we extend the default_get from odoo core models 
    """
    @api.model
    def default_get(self, fields_list):
        import pudb
        pudb.set_trace()
        result = super(ProjectTodoStats, self).default_get(fields_list=fields_list)
        project_todo_stat_model = self.env['project.todo.stats']
        current_stat_obj = project_todo_stat_model.browse(self.env.context['params']['id'])
        # EXERCISE remove the .id from user and interpret error message

        result['user_id'] = current_stat_obj.user_id.id
        result['from_date'] = current_stat_obj.from_date
        return result


    def do_stats(self):
        import pudb
        pudb.set_trace()
        return True


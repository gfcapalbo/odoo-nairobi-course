# -*- coding: utf-8 -*-

import datetime
from odoo import api, models, fields



# wizard that given date and user, calculates the stats for that user

# how many done 
# how many created by him
# how many created that where given to him



# A TRANSIENT MODEL is just like a normal model. but it's existence in the database 
# has a limited timespan. The transient model record will be removed after 


class ProjectTodoStats(models.TransientModel):
    
    _name = "project.todo.stats"
    _description = " statistics for project todo"

    user_id = fields.Many2one('res.users', string='Stats Of')
    from_date = fields.Date(string='After Date')
    how_many_urgent = fields.Integer(string='Urgent Todos')
    how_many_i_made = fields.Integer(string='Todos Created')
    how_many_are_mine = fields.Integer('Todos assigned')


    def launch_stats(self):
        """
        functions can return actions, it's a valid alternative 
        to using menues to launch actions. and can be used to implement 
        multi popup types of situations (your context will follow you around)
        """
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
        current_stat_obj = None
        result = super(ProjectTodoStats, self).default_get(fields_list=fields_list)
        project_todo_stat_model = self.env['project.todo.stats']
        # exercise breakpoint here :  Trace and view context
        if self.env.context.get('active_id', False) and \
                self.env.context.get('active_model', False) == 'project.todo':
            current_stat_obj = project_todo_stat_model.browse(
                    self.env.context['active_id'])
        elif 'id' in self.env.context.get('params').keys():
            current_stat_obj = project_todo_stat_model.browse(self.env.context['params']['id'])
        # EXERCISE remove the .id from user and interpret error message
        if current_stat_obj:
            result['user_id'] = current_stat_obj.user_id.id
            result['from_date'] = current_stat_obj.from_date
        return result


    def do_stats(self):
        from_domain = ()
        user_domain = ()
        if self.from_date:
            from_domain = ('create_date', '>' , self.from_date)
        if self.user_id:
            # EXERCISE : explain
            user_domain = ('user' , '=', self.user_id.id)
        todo_model = self.env['project.todo']
        domain_urgent =  [('is_urgent', '=', True)] 
        domain_how_many_i_made = [('create_uid' , '=', self.user_id.id)]
        domain_how_many_are_mine = [('user', '=', self.user_id.id)]
        if from_domain:
            domain_urgent.append(from_domain)
            domain_how_many_i_made.append(from_domain)
            domain_how_many_are_mine.append(from_domain)
        if user_domain:
            domain_urgent.append(user_domain)
        how_many_urgent = len(todo_model.search(domain_urgent))
        how_many_i_made = len(todo_model.search(domain_how_many_i_made))
        how_many_are_mine = len(todo_model.search(domain_how_many_are_mine))
        self.write({
            'how_many_urgent' : how_many_urgent,
            'how_many_i_made' : how_many_i_made,  
            'how_many_are_mine' : how_many_are_mine,
        })
        return {
                'type': 'ir.actions.act_window',
                'res_model':  'project.todo.stats',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                # EXERCISE : EXPLAIN
                "view_id": self.env.ref('project_todo.project_todo_stats_form_results').id,
                "res_id": self.id
        }

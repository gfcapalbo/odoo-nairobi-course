# -*- coding: utf-8 -*-

import datetime
from odoo import models



# wizard that given date and user, calculates the stats for that user

# how many done 
# how many created by him
# how many created that where given to him
# How many modified by him



class ProjectTodoStats(models.TransientModel):
    
    _name = "project.todo.stats"
    _description = " statistics for project todo"

    user_id = fields.Date()
    date = fields.Date()


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


    def do_stats(self):


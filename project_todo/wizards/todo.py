# -*- coding: utf-8 -*-

import datetime
from odoo import api, models, fields



# wizard that given date and user, calculates the stats for that user

# how many done 
# how many created by him
# how many created that where given to him
# How many modified by him



class ProjectTodo(models.Model):

    _inherit = 'project.todo'
    """
    EXERCISE TRANSIENT to Model  Try making thi transient and see the mess that happens
    """

    """Note we are appling inheritance on our own model.
    in order to have the definition available, verify that the import
    of this wizard happens AFTER the import of the model it inherits in the imports 
    of the module.
    
    We do this for two reasons
        a) the button launch stats is on a form of project.todo. so the function it calls must
        be of this type.
        b) we do not put it in our project.todo class in /models   
        directly to keep a orderly separation between 
        wizard functionality and non-wizard functionality. this is just a style choice.
    """




    @api.multi
    def launch_stats(self):
        self.ensure_one()
        """
        functions can return actions, it's a valid alternative 
        to using menues to launch actions. and can be used to implement 
        multi popup types of situations (your context will follow you around)
        """
        return {
                'type': 'ir.actions.act_window',
                'res_model':  'project.todo.stats',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
        }


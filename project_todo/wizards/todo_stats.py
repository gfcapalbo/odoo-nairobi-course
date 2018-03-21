# -*- coding: utf-8 -*-

import datetime
from odoo import models



# wizard that given date and user, calculates the stats for that user

# how many done 
# how many created by him
# how many created that where given to him
# How many modified by him
#
class ProjectTodoStats(models.TransientModel):
    
    _name = "project.todo.stats"
    _description = " statistics for project todo"

    user_id = fields.date()
    date = fields.Date()




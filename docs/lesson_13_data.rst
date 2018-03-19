Python Inheritance
------------------

Normal python inheritance, while may used when programming with odoo is not what we mean by 'inheritance'when referring to odoo.
The ORM , in the model package offers a type of  inheritance with many extra features and possibilities.

This allows us to plug in existing methods of existing modules,
puggling in may be limited by the poor modularization of the original method(s), and may require an MR to the core module to improve that.




Model  (odoo) Inheritance 
-------------------------


Classical inheritance

When using the _inherit and _name attributes together, Odoo creates a new model using the existing one (provided via _inherit) as a base. The new model gets all the fields, methods and meta-information (defaults & al) from its base.::

       
                inherit='sale.order'
               _name='sale.order.gio'

        wil create a class of models.Model different from sale.order,but with all it's attributes.



Extension   [ most common]

When using _inherit but leaving out _name, *or explictly setting _name the same* the new model replaces the existing one, essentially extending it in-place. This is useful to add new fields or methods to existing models (created in other modules), or to customize or reconfigure them (e.g. to change their default sort order):



Delegation

The third inheritance mechanism provides more flexibility (it can be altered at runtime) but less power: using the _inherits a model delegates the lookup of any field not found on the current model to "children" models. The delegation is performed via Reference fields automatically set up on the parent model:

https://github.com/OCA/OCB/blob/10.0/addons/product/models/product.py#L110


we have here 1 delegation and 1 Classical inheritance on product.product

product.product delegates on product_template via product_tmpl_id field.
the class also inherits 'mail.thread' (as many other classes do) inheriting completely attl the attributes  
and methods needed for the threads we see in the interface under the forms.


When creating custom modules , the extensions are the most common inheritance needed.
Method ovverriding by replacing the original method in odoo seems like an extremly rare usecase , what we want is an extension.

    An example:
      -    in the model sale.order we want to extend creation, after creating the sale order, we want to also set the value of   a new field we added.
        so we create a folder in /models and define a class that inherits models.Model. (python inheritance)


A simple example of inheritance in project
__________________________________________

original project.project class:
https://github.com/OCA/OCB/blob/10.0/addons/project/models/project.py


Project project class is inherited in module project_issue
https://github.com/OCA/OCB/blob/10.0/addons/project_issue/models/project_project.py



We will use inheritance in our TODO module
------------------------------------------

after adding a module dependency to project (where the model we are iheriting is defined)::


   class ProjectProject(models.Model):
       _name = 'project.project'    #OR NOTHING IS BETTER (less possibilities of mistakes)
       _inherit = 'project.project'
       # now we add a couple of fields

       todo_count = fields.boolean(compute=_compute_has_todos)
       associated_todos = fields.Many2many('project.todo')

       # we could  now  show these fields in ANY view that is of model project.project
       # we will see this in the  view inheritance lesson this afternoon, in the meantime we will
       # add them toa view via interface.
       # ADD FIELDS TO INTERFACE


PARTIAL MODIFICATION OF FIELD MODIFICATION
__________________________________________


if you have a field that already exists , by redefining it you can change or add only some of it's attributes.

 color = fields.integer(required=True)    # now all projects must have a color.



how to use odoo inheritance to extend create() - calling super()
----------------------------------------------------------------


SUPER
-----
Super is used to return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. The search order is same as that used by getattr() except that the type itself is skipped.”

the super function can be used to gain access to inherited methods – from a parent or sibling class – that has been overwritten in a class object.

A simple example of super in python:

        https://www.programiz.com/python-programming/methods/built-in/super

(the __init__ function is a special function, a *constructor* , something that happens when we create an instance of the class we are describing)


THe official super documentation:

        https://docs.python.org/2/library/functions.html#super

In odoo:::
        
        super(classname, self).method()  will call and return the method() of it's parent.
        

        This is managed by odoo. "Normal" python super would call the method of the class it inherits, in our case only model.Models. But the odoo framework manages inheritance by checking the attribute inheritand will find our parent class.





logical placement of super. In writes. In Creates.
--------------------------------------------------

write and create pseudo-code::

    @api.multi
    def write(self, vals):
        code code code probably modifying vals
        # Now we call super, the parent write that has been overwritten
        # the super chain should not be broken
        res=super(ProjectProject, self)
        code code , probably using "res"
        return res
        
    @api.model
    def create(self):
        # Now we call super, theparent write that has been overwritten
        # the super chain should not be broken
        res=super(ProjectProject, self)
        code code , probably using "res"
        return res
::

Let's overwrite create and write in our project extension
_________________________________________________________



OBSERVATIONS
------------

-Any method in the parent class can be overwitten and modified.
-Poor modularity of the parent function structure may cause difficulties, and force us to present an MR to the parent module.
- the logical order of calls is determined by the module inheritance chain


GROUP EXERCISE:

Project project model definition in project has some interesting inheritances, read together:
https://github.com/OCA/OCB/blob/10.0/addons/project/models/project.py#L52
and line 53





EXERCISE:

0- make seqence mandatory field in project project, and make it's default 44 , verify in interface.

1- we now have _compute_todo_count to calculate how many todos a project has
   overwrite _compute_task_count  in project.project to become the computed field for  
   todo_count

2 - Extend res users and add whatever you please to it


3- implement some sort of 'default'  by overwriting create and explain why is this worse than using the default attribute in the field definition.

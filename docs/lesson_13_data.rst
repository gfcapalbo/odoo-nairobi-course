Python Inheritance
------------------

Normal python inheritance, while may used when programming with odoo is not what we mean by 'inheritance'when referring to odoo.
The ORM , in the model package offers a type of  inheritance with many extra features and possibilities.
THis allows us to plug in existing methods of existing 

THis approcach may be limited by the poor modularization of the original method(s), and may require an MR to the core module to improve that.




Model  (odoo) Inheritance 
-------------------------


Classical inheritance

When using the _inherit and _name attributes together, Odoo creates a new model using the existing one (provided via _inherit) as a base. The new model gets all the fields, methods and meta-information (defaults & al) from its base.

                so :   inherit='sale.order'
                        _name='sale.order.gio'

        wil create a class of models.Model different from sale.order,but with all it's attributes.



Extension   [ most common]

When using _inherit but leaving out _name, *or explictly setting _name the same* the new model replaces the existing one, essentially extending it in-place. This is useful to add new fields or methods to existing models (created in other modules), or to customize or reconfigure them (e.g. to change their default sort order):



Delegation

The third inheritance mechanism provides more flexibility (it can be altered at runtime) but less power: using the _inherits a model delegates the lookup of any field not found on the current model to "children" models. The delegation is performed via Reference fields automatically set up on the parent model:

https://github.com/OCA/OCB/blob/10.0/addons/product/models/product.py#L110


we have here 1 delegation and 1 Classical inheritance on product.product

product.product delegates on product_template via product_tmpl_id field.
the class also inherits 'mail.thread' (as many other classes do) inheriting completely attl the attributes  and methods needed for the threads we see in the interface under the forms.


When creating custom modules , the extensions are the most common inheritance needed.




how to use odoo inheritance to extend create() - calling super()
----------------------------------------------------------------
We refer to extension inheritance.


Method ovverriding by replacing the original method in odoo seems like an extremly rare usecase , what wewant is an extension.


- logical placement of super. In writes. In Creates.


_usecase:





ir.sequence
-----------

The Odoo Exceptions structure: raise ValidationError 
----------------------------------------------------
When an exception is raised in python,  it propagates up the call stack,
In Odoo, the RPC layer that answers the calls made by the web client catches all exceptions
and, depending on the exception class, it will trigger different possible behaviors on the
web client.








- selection_add
---------------

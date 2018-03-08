
Module  - Module structure basic 2
   Data files XML
   record and menuitem and <data noupdate="1">
   actwindow ans domains
   Security groups
   Creating Module Data, 
   XMLID/external id, 
   self.env.ref()
   When is data installed? difference between -u (update) and -i  (/initialization), 
   ----Exercise: Add data from this morning into a module
   ----Exercise: Add to project_todo  a) a project b) a set of completed tasks c) a set of tasks to complete


  In this lesson we will learn how to add hardcoded data to our module. Data we can rely on in our program, use
  and refer to in our code. 

  There are many reasons one might want this: Eg. hardcoded Accounting charts, Hardcoded Categories or Hardcoded website charateristics.

  Data can also be used to modify existing data from previous models of wich we know the existence.

  The " data " structure in odoo, in canonical module structure is placed in the /data directory. Not because it is significantly 
  different from other XML records we have previously discussed but to logically order them and distinguish them from views and templates.

  Data XML's must be included in the manifest under the 'data' key.


  The XMLID is an unique unifier for a record in a database. It is assigned and managed by the Odoo framework and accessible to the programmer by knowing simple rules about it's nomenclature.
  An id is a record of model ir.model.data

  https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/ir/ir_model.py#L982


  An XML_ID follows the momenclature  {ModuleName}.{RecordName} and can be declared both with it's complete name ( like sale.myview) or incomplete name
  a myview record


  A data record is declared as so in our /data file

  <record id="project_todo.mydata" model="somemodel">

  <record>

  or:

  <record id="mydata" model="somemodel">

  <record>

  *in the project_todo module*

  As you can see: the unique and fully qualifying  XMLID of this record is  "project_todo.mydata" , and is aoutocompleted here if not completely given:

  https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/ir/ir_model.py#L1009

  Also note that we have given the ID and the model in this record, wich are the only  
  required fields in the model.

  noupdate = fields.Boolean(string='Non Updatable', default=False)
  model = fields.Char(string='Model Name', required=True)

  also 'module' is required. But the module as we said before is inferred by the placement of the record itself.
  If it is in sale we know it wil be sale.XXXXX , if it is in project_todo we know it will be called project_todo.xxxxx


  As you can see the odoo Framework is used internally to implement parsers, interpreters and models for supporting data structures.

 
  Data records can be used to modify or create ir.model.data records.
  If the full XML_ID exists the definition modifies the existing record. If it does not exist it creates a new record.

  For example, if in our project_todo we create a record:

<record id = "project.mt_task_new" model="mail.message.subtype">
<field name="name">Task Opened!</field>

</record>

we are modifying :

  https://github.com/OCA/OCB/blob/10.0/addons/project/data/project_data.xml#L39

  and changing it's name from Task Opened to Task Opened!

  In this case we must be sure that project_todo depends on 'project'

but if we write in our module :

<record id = mt_task_new" model="mail.message.subtype">
        <field name="name">Task Opened!</field>
</record>

We are creating a new record with unique XML ID "project_todo.mt_task_new" and it will generate an error , because not all required fields of the model
"mail.message.subtype" are defined and it will be impossible to create a new record.



  THe order with wich the XML IDS are evaluated is decided by the module inheritance tree. So if you are modifying an existing Data record or if you 
  refer to an existing data record, make sure your module depends on the module that conains the definition of the data record you change/refer to.

  In this way you are sure the data you need is already loaded when you start creating yours.

  Wrong inheritance definition is a common source of bugs.




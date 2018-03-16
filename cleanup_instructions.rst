Cleanup Instructions
--------------------

THese clenaup instructions are for all students, before learning git.
THe objective is to have all the same enviroment and use giovanni's todo module and
terrence's trip module simultaneusly.

THe objective is to have the students manage correctly their addon paths.

we will touch upon basic GIT commands, some psql, and some odoo server configuration management.

GET THE VERSION WITH TODO Module


        cd                                                                                        //      (go to home)
        git clone https://github.com/gfcapalbo/odoo-nairobi-course/   odoo-nairobi-todoprj        //  clone our repository andcreate this directory
        cd odoo-nairobi-todoprj                                                                   // enter direcotory
        git checkout lesson_9                                                                     // lesson_9 is the latest version of your
        cd ..

GET THE VERSION WITH TRIP MODULE

        cd            (go to home)
        git clone https://github.com/gfcapalbo/odoo-nairobi-course/   odoo-nairobi-tripprj
        cd odoo-nairobi-tripprj
        git checkout lesson_8                                                                     // lesson 8 is the latest version od terrence's trip module
        cd ..
        



Now all students have a consistent directory structure  and can install TRIP module and TODO module


{your_home_location}/{odoo location}/addons,                                              // Here are all odoo addons
{your home location}/{odoo_location}/odoo/addons,                                         // here are all odoo core addons (installed by default)
{your_home_location}/odoo-nairobi-tripprj,                                                // here lives terrence's trip module
{your_home_location}/odoo-nairobi-todoprj                                                 // here lives giovanni's todo module



Now we need a configuration file that uses these locations:

so put in  {your_odoo_location}/debian/odoo.conf


addons_path = {your_home_location}/{odoo location}/addons, {your home location}/{odoo_location}/odoo/addons, {your_home_location}/odoo-nairobi-tripprj, {your_home_location}/odoo-nairobi-todoprj



All on one line , no spaces.




Or configure your PYCHARM in a way to use this 




DATABASES
---------

A fresh database when starting odoo programming and changing often the code is necessary

so from the command line:



createdb o10                                     // creates a DB 


from {your_odoo_location} run:


python odoo-bin   -d o10  -c debian/odoo.conf  



Or run  your PYCHARM configuration to run this.


        SOME DB OPERATIONS
        ------------------

        createdb o10                      //create a empty db called o10
        dropdb o10                        // delete the db called o10
        psql -l                           // show all the databases on my system
        psql o10                          // enter the database to write queries and see the data




ODOO PARAMETERS
---------------

        -d  {database name}
        -c {configuration file}
        -u  {module name}




IMPORTANT HOW TO USE THE DIRECTORY STRUCTURE
--------------------------------------------


Until more git commands have been done, do not change anything in 

{your_home_location}/odoo-nairobi-tripprj
{your_home_location}/odoo-nairobi-todoprj


And when an update is provided by the teacher just enter the directory and write

git pull

you will receive the new code.




PERSONAL PLAYGROUND
___________________

MAke your own directory and create a new module, in a separate directory.
Add the directory to conf file.
You cna write your code easily there whithout interfering with trip module and todo module.
As we explain git branches and pushes, you will aso be able to send them remotely , but in general good separation of projects is important.












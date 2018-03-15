 Python Basics:

	Flake8

		sudo apt-get install flake8
		use:
			flake8 my_program.py

	Datatypes : int , float, str, list, tuple, dictionary

	Indentation

	functions

		def sum(a,b):
		    c=a+b
		    return c

	Isinstance
		isinstance(c, int)
                isinstance(c, str)

	Essential Python core functions

	  https://docs.python.org/2/library/functions.html

	Python types
          https://docs.python.org/2/library/stdtypes.html


        do not use random websites , but allways refer to docs.python.org

       classes
          

           see code classes.py for example of a class, instances, use of self.

           self is NOT a keyword. It could be any name. Self is good code for clarity
           because it indicates well it refers to the instance itself

       Arguments and keyword arguments
       -------------------------------
        Python can have 2 types of arguments : normal arguments and keyword arguments as so:

        def myfunction(a, b , double=True)
                c=a+b
                if double:
                    c=c*2
                return c


        in this example we have 2 normal aruments and 1 keyword argument.
        the function can be called as so:

        myfunction(1, 2)
        myfunction(1, 2, True)
        myfunction(1,2, double=True)

        - it is best practice to explictly  express the keyword name.
        - The value of keyword attrbute  is NOT the value of the attribute, but it's
          DEFAULT in case it is not specified in the function signature.

        keyword patterns allow us to have optional parameters with defaults.
        
        we can have a random amount of arguments by putting (star)args in the
        signature and a random amount of keyword arguments by putting 
        (star)(star)kwargs in the function signature



        REFERENCES:

        INTRODUCTION TO CLASSES: https://docs.python.org/2/tutorial/classes.html  
        CORE FUNCTIONS (LEARN MOST): https://docs.python.org/2/library/functions.html



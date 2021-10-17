# Solve-Quadratic-or-first-level--equations
My first repository on GitHub

The file RunRealsComplexRoots.py will solve any complete quadratic equation a*x² + b*x + c = 0 and will get two reals or complexs roots of quadratic equation. Too will solve any incomplete quadratic equation as: a*x² + b*x = 0 if coefficient c = 0 or a*x² + c = 0 if the coefficient b = 0 and will two reals or complexs roots and too will solve any first level equation as: a*x + b = 0. When run the file RunRealsComplexRoots.py into Python3-Idle3 or any other IDE provide new values to the coefficients: a = ?, b = ? and c = ? to solve any complete quadratic equation. To solve any equations of the first level run the file RunRealsComplexRoots.py and provide the coefficients: a = 0, b = ? and c = ?. If be in Windows operating system open the Python Interpreter before of run the RunRealsComplexRoots.py.

For example see the use of the file RunRealsComplexRoots.py below:

1.) If the delta discriminant is positive( delta > 0)

Python 3.8.10 (default, Sep 28 2021, 16:10:42) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /home/cristovom/Python-3.8.5-LabDev-2020/Module-Tools/RunRealsComplexRoots.py


	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.0 -- [ Stable ] _-_
		    [Developed by Cristovom A. Girodo]



	* Provide the 1º [coefficient].
	-_- What is the new value? -3

	* Enter with the 2º [coefficient].
	-_- What is the new value? 12

	* Give the 3º [coefficient].
	-_- What is the new value? 27


		============================================
		| . . . *[ ANSWER TO THE EQUATION ]* . . . |
		============================================


   + The new value of [delta] =  468
   + The value of the [raisedelta] =  21.63     

   + The [roots] are:  
   + The first  root(root1)= -1.61      
   + The second root(root2)= 5.61      


  =====================================================================
  |º>º If necessary process the RealsComplexRoots.py module again! º>º|
  =====================================================================


		 . . .Key [ENTER] to exit, Ok!. . .
		 
		 
2.) If the delta discriminant is zero( delta = 0)

= RESTART: /home/cristovom/Python-3.8.5-LabDev-2020/Module-Tools/RunRealsComplexRoots.py


	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.0 -- [ Stable ] _-_
		    [Developed by Cristovom A. Girodo]



	* Provide the 1º [coefficient].
	-_- What is the new value? -1

	* Enter with the 2º [coefficient].
	-_- What is the new value? 4

	* Give the 3º [coefficient].
	-_- What is the new value? -4


		============================================
		| . . . *[ ANSWER TO THE EQUATION ]* . . . |
		============================================


   + The new value of [delta] =  0

   + The [roots] are:  
   + The first  root(root1)= 2.00       
   + The second root(root2)= 2.00      


  =====================================================================
  |º>º If necessary process the RealsComplexRoots.py module again! º>º|
  =====================================================================


		 . . .Key [ENTER] to exit, Ok!. . .
		 
		 
3.) If the delta discriminant is negative( delta < 0) will get two complexs roots of the complete quadratic equation

= RESTART: /home/cristovom/Python-3.8.5-LabDev-2020/Module-Tools/RunRealsComplexRoots.py


	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.0 -- [ Stable ] _-_
		    [Developed by Cristovom A. Girodo]



	* Provide the 1º [coefficient].
	-_- What is the new value? 3

	* Enter with the 2º [coefficient].
	-_- What is the new value? 5

	* Give the 3º [coefficient].
	-_- What is the new value? 6


		============================================
		| . . . *[ ANSWER TO THE EQUATION ]* . . . |
		============================================


   + The new value of [delta] =  -47

   --------------------------------------------------------------------
   * When the value of delta is negative the equation: a*x**2+b*x+c = 0
            to theorem have not reals roots. *
   --------------------------------------------------------------------


	   * Will get only two complexs roots *

   + The value of the [raisedelta] =  0.00+6.86j

   + The [roots] are:  
   + The first  root(root1)= -0.83+1.14j 
   + The second root(root2)= -0.83-1.14j


  =====================================================================
  |º>º If necessary process the RealsComplexRoots.py module again! º>º|
  =====================================================================


		 . . .Key [ENTER] to exit, Ok!. . .
		 
		 
4.) Incomplete quadratic equation 

= RESTART: /home/cristovom/Python-3.8.5-LabDev-2020/Module-Tools/RunRealsComplexRoots.py


	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.0 -- [ Stable ] _-_
		    [Developer: Cristovom A. Girodo]



	* Provide the 1º [coefficient].
	-_- What is the new value? 8

	* Enter with the 2º [coefficient].
	-_- What is the new value? -16

	* Give the 3º [coefficient].
	-_- What is the new value? 0


		============================================
		| . . . *[ ANSWER TO THE EQUATION ]* . . . |
		============================================


  - The new equation of the second level geted will an of the followings:
    [ a*x**2+b*x = 0 or -a*x**2-b*x = 0 or a*x**2-b*x = 0 or -a*x**2+b*x = 0 ]
      and will have two reals roots.


   + The [roots] are:  
   + The first  root(root1)= 0.00       
   + The second root(root2)= 2.00      


  =====================================================================
  |º>º If necessary process the RealsComplexRoots.py module again! º>º|
  =====================================================================


		 . . .Key [ENTER] to exit, Ok!. . .
		 
5.) The solution of the first level equation 

= RESTART: /home/cristovom/Python-3.8.5-LabDev-2020/Module-Tools/RunRealsComplexRoots.py


	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.0 -- [ Stable ] _-_
		    [Developed by Cristovom A. Girodo]



	* Provide the 1º [coefficient].
	-_- What is the new value? 0

	* Enter with the 2º [coefficient].
	-_- What is the new value? 54

	* Give the 3º [coefficient].
	-_- What is the new value? -118


		============================================
		| . . . *[ ANSWER TO THE EQUATION ]* . . . |
		============================================


  - The new equation of the first level geted will: [ b*x+c = 0 ]
    and will have an only real root.


	+ The new real root will:  -2.19     


  =====================================================================
  |º>º If necessary process the RealsComplexRoots.py module again! º>º|
  =====================================================================


		 . . .Key [ENTER] to exit, Ok!. . .

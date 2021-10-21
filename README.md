# Solve-Quadratic-or-first-level--equations
My first repository on GitHub

The file RunRealsComplexRoots.py will solve any complete quadratic equation a*x² + b*x + c = 0 and will get two reals or complexs roots of quadratic equation. Too will solve any incomplete quadratic equation as: a*x² + b*x = 0 if coefficient c = 0 or a*x² + c = 0 if the coefficient b = 0 and will get two reals or complexs roots. When run the file RunRealsComplexRoots.py into Python3-Idle3 or any other IDE provide new values to the coefficients: a = ?, b = ? and c = ? to solve any complete quadratic equation. The coefficients: a, b and c will can be positive or negative or equal the zero. When use the file RunRealsComplexRoots.py to solve incomplete or complete quadratic equations; but never use all the coefficients: a = b = c = zero. Too will solve any first level equation as: b*x + c = 0. To solve any equations of the first level run the file RunRealsComplexRoots.py and provide the coefficients: a = 0, b = ? and c = ?. The coefficients: b and c will can be positive or negative, but never use all the coefficients: b = c = zero. The file RunRealsComplexRoots.py will run into the Windows operating system without any change. With the new Version: 4.2, the file RunRealsComplexRoots.py will solve any incomplete quadratic equation: a*x² + 0*x + 0 = 0 if b = c = 0 and too any incomplete first level equation: b*x + 0 = 0 if c = 0. In both previous incomplete equations always will get all the roots: root1 = 0, root2 = 0 and root = 0.

# Instructions of use: 
# 1.) To run the file RunRealsComplexRoots.py will into the Windows operating system, copy the file RunRealsComplexRoots.py to any directory and give a two click.
# 2.) After, follow the informations of this program into the display.
# 3.) In any Linux operating system, open the file RunRealsComplexRoots.py using the editor IDLE and after click in Run --> Run module and follow the informations       of this program into the display.
# [ Warning! ] 
# Run only the file RunRealsComplexRoots.py to get the roots: the root1, root2 and root. The file RunRealsComplexRoots.py will run too the RealsComplexRoots.py    module.

# Note: In 20211019 the files: RunRealsComplexRoots.py and RealsComplexRoots.py was update -- Version: 4.1
# Note: In 20211021 the files: RunRealsComplexRoots.py and RealsComplexRoots.py was update -- Version: 4.2 

For example see the use of the file RunRealsComplexRoots.py below:

# 1.) If the delta discriminant is positive( delta > 0)

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
		 _-_ New Version: 4.2 -- [ Stable ] _-_
		    [Developed by Cristovom A. Girodo]



	* Provide the 1º [coefficient(a)].
	-_- What is the new value? -3

	* Enter with the 2º [coefficient(b)].
	-_- What is the new value? 12

	* Give the 3º [coefficient(c)].
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
		 
		 
# 2.) If the delta discriminant is zero( delta = 0)

	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.2 -- [ Stable ] _-_
		    [Developed by Cristovom A. Girodo]



	* Provide the 1º [coefficient(a)].
	-_- What is the new value? -1

	* Enter with the 2º [coefficient(b)].
	-_- What is the new value? 4

	* Give the 3º [coefficient(c)].
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
		 
		 
# 3.) If the delta discriminant is negative( delta < 0) will get two complexs roots of the complete quadratic equation

	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.2 -- [ Stable ] _-_
		    [Developed by Cristovom A. Girodo]



	* Provide the 1º [coefficient(a)].
	-_- What is the new value? 3

	* Enter with the 2º [coefficient(b)].
	-_- What is the new value? 5

	* Give the 3º [coefficient(c)].
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
		 
		 
# 4.) Incomplete quadratic equation 

	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.2 -- [ Stable ] _-_
		    [Developer: Cristovom A. Girodo]



	* Provide the 1º [coefficient(a)].
	-_- What is the new value? 8

	* Enter with the 2º [coefficient(b)].
	-_- What is the new value? -16

	* Give the 3º [coefficient(c)].
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
		 
# 5.) The solution of the first level equation 

	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.2 -- [ Stable ] _-_
		    [Developed by Cristovom A. Girodo]



	* Provide the 1º [coefficient(a)].
	-_- What is the new value? 0

	* Enter with the 2º [coefficient(b)].
	-_- What is the new value? 54

	* Give the 3º [coefficient(c)].
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

# 6.) If the coefficients: a = b = c = 0 see below:

= RESTART: /home/cristovom/Python-3.8.10-Lab/Module-Tools/RunRealsComplexRoots.py

	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.2 -- [ Stable ] _-_
		    [Developed by Cristovom A.Girodo]



	* Provide the 1º [coefficient(a)].
	-_- What is the new value? 0

	* Enter with the 2º [coefficient(b)].
	-_- What is the new value? 0

	* Give the 3º [coefficient(c)].
	-_- What is the new value? 0


	 //////
	(º < º) [ WARNING! ]
	 \ - /
	** [ No exist none complete quadratic equation: [ a*x**2+b*x+c = 0 ] when the coefficients: a = 0, b = 0 and c = 0 and
	     too none first level equation: [ b*x+c = 0 ] to solve--Ok! ]**
	-- [ Enter with [New values] to the [ coefficients: a = ?, b = ? and c = ? ]--


	* Provide the 1º [coefficient(a)].
	-_- What is the new value? -3

	* Enter with the 2º [coefficient(b)].
	-_- What is the new value? 22

	* Give the 3º [coefficient(c)].
	-_- What is the new value? 35


		============================================
		| . . . *[ ANSWER TO THE EQUATION ]* . . . |
		============================================


   + The new value of [delta] =  904
   + The value of the [raisedelta] =  30.07     

   + The [roots] are:  
   + The first  root(root1)= -1.34      
   + The second root(root2)= 8.68      


  =====================================================================
  |º>º If necessary process the RealsComplexRoots.py module again! º>º|
  =====================================================================


		 . . .Key [ENTER] to exit, Ok!. . .
		 
# 7.) If the coefficients: a = ? and b = c = 0 see below:

=============== RESTART: /home/cristovom/RunRealsComplexRoots.py ===============


	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.2 -- [ Stable ] _-_
		    [Developed by Cristovom A.Girodo]



	* Provide the 1º [coefficient(a)].
	-_- What is the new value? 3

	* Enter with the 2º [coefficient(b)].
	-_- What is the new value? 0

	* Give the 3º [coefficient(c)].
	-_- What is the new value? 0


		============================================
		| . . . *[ ANSWER TO THE EQUATION ]* . . . |
		============================================


	**[ Have a incomplete quadratic equation: ]**
	[ a*x**2+0*x+0 = 0 ] ==> [ a*x**2 = 0 ] ==> [ x**2 = 0 / a ] ==> [ x**2 = 0 ] ==> [ x = root1 = root2 = zero ]

   + The [roots] are:  
   + The first  root(root1)= 0.00       
   + The second root(root2)= 0.00      


  =====================================================================
  |º>º If necessary process the RealsComplexRoots.py module again! º>º|
  =====================================================================


		 . . .Key [ENTER] to exit, Ok!. . .
		 
# 8.) If the coefficients: a = 0, b = ? and c = 0 see below:

=============== RESTART: /home/cristovom/RunRealsComplexRoots.py ===============



	========================================================
	  [   Welcome using The RealsComplexRoots.py module  ]
	--------------------------------------------------------
	 -_- Find the roots: root1 and root2 reals or complexs 
	========================================================
		 _-_ New Version: 4.2 -- [ Stable ] _-_
		    [Developed by Cristovom A.Girodo]



	* Provide the 1º [coefficient(a)].
	-_- What is the new value? 0

	* Enter with the 2º [coefficient(b)].
	-_- What is the new value? 23

	* Give the 3º [coefficient(c)].
	-_- What is the new value? 0


		============================================
		| . . . *[ ANSWER TO THE EQUATION ]* . . . |
		============================================


	**[ Have a incomplete first level equation: ]**
	[ b*x+0 = 0 ] ==> [ b*x = 0 ] ==> [ x = 0 / b ] ==> [ x = 0 ] ==> [ x = root = zero ]


	+ The new real root will:  0.00      


  =====================================================================
  |º>º If necessary process the RealsComplexRoots.py module again! º>º|
  =====================================================================


		 . . .Key [ENTER] to exit, Ok!. . .
		 
# Good Luck! the all in using the file RunRealsComplexRoots.py that created.


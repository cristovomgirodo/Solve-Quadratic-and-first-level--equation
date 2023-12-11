############################################################################
#
#	The AlgQuadratic_FirstLevel_Equation.py module
#	Will find the [ Reals(|R) and Complexs(C) Roots of the Equations.
#	-----------------------------------------------------------------------	
#	Developed by Cristovom A. Girodo  
#	Data: 28/07/2023  --  Version: 5.0 (Stable)
#
############################################################################

import math
import cmath 

class Quadratic_FirstLevel_Equation:
	def __init__(self, coef_a=0, coef_b=0, coef_c=0, discriminante=0, raisedelta=0, root=0, root1=0, root2=0):
		self.coef_a = coef_a
		self.coef_b = coef_b
		self.coef_c = coef_c
		
	def introduce(self):
		while True:
			try:
				coeffic = float(input('\t -_- Type the [new] value? '))
				return coeffic
			except ValueError as err:
				print('\n\t   _/=\_')
				print('\t    º<º  [Warning!]:',err)
				print('\t    \~/  [ TYPE AN NEW [POSITIVE OR NEGATIVE OR ZERO] FLOAT NUMBER ]')
				print('\t         [ IN NEXT INSTRUCTION -- OK! ]\n')
                   	
	def getcoeficientes(self):
		# função: novocoeficinte() created as sub-rotina of getcoeficientes(self) method.
		def novocoeficinte():
			valor = self.introduce()
			print(f'\t----------------------------------------\n')
			return valor
			
		for j in range(1,4):
			if j == 1:
				print(f'\n\t*[Enter [news] Coefficients of the Quadratic Equation]*')	
				self.coef_a = novocoeficinte()
			elif j == 2:
				print(f'\t   - The {j}º [coefficients(b)]: ')
				self.coef_b = novocoeficinte()
			elif j == 3:
				print(f'\t   - The {j}º [coefficients(c)]: ')
				self.coef_c = novocoeficinte()
				if self.coef_a != 0 and self.coef_b != 0 and self.coef_c != 0:
					print('\t--[ [reals] Coefficients typed, Ok!]--\n')	
					
				while self.coef_a == 0 and self.coef_b == 0 and self.coef_c == 0:
					print('\n\t\t_|=*=|_	')
					print('\t\t º < º	 **[ Warning! ]**')
					print('\t\t \ ~ /	--[ No exist this Quadratic Equation: 0*x² + 0*x + 0 = 0 ]--\n')
					self.coef_a, self.coef_b, self.coef_c = self.getcoeficientes()
		
		return self.coef_a, self.coef_b, self.coef_c  # is necessary the return of this local variables
			
	def getcoefA(self):
		return self.coef_a
	
	def getcoefB(self):
		return self.coef_b
		
	def getcoefC(self):
		return self.coef_c
		
	def answer(self):
		print('\n\t**[Solution]**')
		return
		
	def getDelta(self):
		discriminante = ( ( math.pow(self.coef_b, 2) ) - ( 4 * self.coef_a * self.coef_c) )
		print(f'\t-- The [new] value of [delta] finded is {discriminante:<10.2f}')
		return discriminante
		
	def getRaiseDelta(self):
		discriminante = self.getDelta()
		if discriminante < 0:
			raisedelta = cmath.sqrt(discriminante)
		else:
			raisedelta = math.sqrt(discriminante)
		print(f'\t-- The value of [raisedelta] calculed is {raisedelta:<10.2f}')
		return discriminante, raisedelta	# is necessary the return of this local variables
		
	def getRoot(self):
		
		def viewRoot():
			print(f'\n\t-- The [real root] determined is {root:<10.2f}')
			return
			
		def viewRealsRoots():
			print(f'\n\t-- The first [real root] is {root1:<10.2f}')
			print(f'\t-- The second [real root] is {root2:<10.2f}')
			return
			
		def viewComplexRoots():
			print(f'\n\t-- The first [complex root] is {root1:<10.2f}')
			print(f'\t-- The second [complex root] is {root2:<10.2f}')
			return
			
		print("\n\t=========================================")
		print("\t| . . . *[ EQUATION PROCESSING ]* . . . |")
		print("\t=========================================\n")
			
		if self.coef_a != 0 and self.coef_b != 0 and self.coef_c != 0:
			
			discriminante, raisedelta = self.getRaiseDelta()	
				
			if discriminante > 0:
				root1 = ( ( (-1) * (self.coef_b) ) + ( math.sqrt(discriminante) ) ) / ( 2 * self.coef_a ) 
				root2 = ( ( (-1) * (self.coef_b) ) - ( math.sqrt(discriminante) ) ) / ( 2 * self.coef_a )
				self.answer() 
				viewRealsRoots()
				
			elif discriminante == 0:
				root = ( ( (-1) * self.coef_b ) / ( 2 * self.coef_a ) )
				self.answer()
				viewRoot()
				
			elif discriminante < 0:
				print(f'\n\t***[WARNING!]***')
				print(f'\t**')
				print(f'\t**[ IF THE VALUE OF [DELTA] IS [NEGATIVE] THEN NO EXIST [REALS(|R) ROOTS]: ROOT1 AND ROOT2] ]**')
				print(f'\t**[ WITH THE COEFICIENTS TYPED OF THIS EQUATION!]**')
				print(f'\t**[ AND WILL FIND THE COMPLEXS(C) ROOTS : ROOT1 E ROOT2 OF THIS EQUATION -- OK! ]**\n')
				root1 = ( ( (-1) * (self.coef_b) ) + ( cmath.sqrt(discriminante) ) ) / ( 2 * self.coef_a ) 
				root2 = ( ( (-1) * (self.coef_b) ) - ( cmath.sqrt(discriminante) ) ) / ( 2 * self.coef_a )
				self.answer() 
				viewComplexRoots()
		
		elif self.coef_a != 0 and self.coef_b == 0 and self.coef_c == 0:
			print('\n\t**[ The coefficients finded an incomplete Quadratic Equation! ]**')
			print('\t[ a*x²+ 0*x + 0 = 0 ] ==> [ a*x² = 0 ] ==> [ x² = 0 / a ] ==> [ x² = 0 ] ==> [ x = root1 = root2 = zero ]')
			root1, root2 = 0, 0
			self.answer()
			viewRealsRoots()
			
		elif self.coef_a > 0 and self.coef_b == 0 and self.coef_c > 0 or self.coef_a < 0 and self.coef_b == 0 and self.coef_c < 0:
			print('\n\t- The [new] incomplete Quadratic Equation are: [ a*x² + 0*x + c = 0 ] or [ -a*x² + 0*x - c = 0 ] ')
			print('\t- and will find two [ complexs roots]: root1 and root2.\n')
			root = - (( self.coef_c + 0.0) / self.coef_a )
			root1 = cmath.sqrt(root)
			root2 = -cmath.sqrt(root)
			self.answer()
			viewComplexRoots()
			
		elif self.coef_a < 0 and self.coef_b == 0 and self.coef_c > 0 or self.coef_a > 0 and self.coef_b == 0 and self.coef_c < 0:
			print('\n\t- The [new] incomplete Quadratic Equation are: [ -a*x² + 0*x + c = 0 ] or [ a*x² + 0*x - c = 0 ] ')
			print('\t- and will calculed two [ reals roots]: root1 and root2.\n')
			root = - (( self.coef_c + 0.0) / self.coef_a )
			root1 = math.sqrt(root)
			root2 = -math.sqrt(root)
			self.answer()
			viewRealsRoots()
			
		elif self.coef_a > 0 and self.coef_b > 0 and self.coef_c == 0 or self.coef_a < 0 and self.coef_b < 0 and self.coef_c == 0 or self.coef_a < 0 and self.coef_b > 0 and self.coef_c == 0 or self.coef_a > 0 and self.coef_b < 0 and self.coef_c == 0:
			 print('\n\t- The [new] incomplete Quadratic Equation are: [ a*x² + b*x + 0 = 0 ] or [ -a*x² - b*x + 0 = 0 ] or ')
			 print('\t- [ -a*x² + b*x + 0 = 0 ] or [ a*x² - b*x + 0 = 0 ] and will determine two [ reals roots]: root1 and root2.\n')
			 root1 = 0
			 root2 = - ( self.coef_b + 0.0 ) / self.coef_a
			 self.answer()
			 viewRealsRoots()
			 
		elif self.coef_a == 0 and self.coef_b != 0 and self.coef_c != 0:
			print('\n\t- The [new] first level Equation is determined when: a = 0 ==> [ b*x + c ] or [ -b*x - c ] or [ b*x - c ] or [ -b*x + c ].\n')
			print('\t- The [real root] will finded by: root = [(- self.coef_c) / self.coef_b] or root = [self.coef_c / ( -self.coef_b)] or')
			print('\t\t\t\t\t  root = [self.coef_c / self.coef_b] or root = [(- self.coef_c) / ( -self.coef_b) ].')
			if self.coef_b > 0 and self.coef_c > 0 or self.coef_b < 0 and self.coef_c < 0:
				root = ( -self.coef_c + 0.0 ) / self.coef_b
			elif self.coef_b > 0 and self.coef_c < 0 or self.coef_b < 0 and self.coef_c > 0:
				root = ( self.coef_c + 0.0 ) / self.coef_b
			self.answer()
			viewRoot()
			
		elif self.coef_a == 0 and self.coef_b != 0 and self.coef_c == 0:
			print('\n\t**The [coefficients] finded an incomplete first level Equation! ]**')
			print('\t [b*x + 0 = 0 ] ==> [ b*x = 0 ] ==> [ x = 0 / b ] ==> [ x = 0 ] ==> [ x = root = zero ]\n')
			root = 0
			self.answer()
			viewRoot()
				
		print(f'\n\n\t--[Algorithm: [RunAlgQuadratic_FirstLevel_Equation.py] ended Ok!]--\n')
		return
		






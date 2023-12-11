###################################################################################################
#
#  The AlgQuadratic_FirstLevel_Equation.py module will find the [reals or complexs roots]: [root1]  
#  or [root2] or [root] of any Quadratic or FirstLevel Equation
#  -----------------------------------------------------------------------------------------------
#  Developed by Cristovom A.Girodo 
#  Date: 20230728  --  New Version: 5.0 (Stable)                                                                             
#                                                              
###################################################################################################

print('\n\n\t=======================================================================')
print('\t|         **[ SOLVE THE QUADRATIC OR FIRSTLEVEL EQUATIONS ]**         |')
print('\t|  -----------------------------------------------------------------  |')
print('\t|  **[ USING THE RUNALGQUADRATIC_FIRSTLEVEL_EQUATIONS.PY PROGRAM ]**  |')
print('\t|  -----------------------------------------------------------------  |')
print('\t|            . . . [ New Version: 5.0 (Stable) ] . . .                |')
print('\t=======================================================================\n')

from AlgQuadratic_FirstLevel_Equation import Quadratic_FirstLevel_Equation

def main():				
	# Create the instance: resolver
	resolver = Quadratic_FirstLevel_Equation()
	resolver.getcoeficientes()		
	# Find the [reals or complexs roots] of the Equation
	resolver.getRoot()
main()

input("\n\n\t\t . . .Key [ENTER] to exit, Ok!. . .")

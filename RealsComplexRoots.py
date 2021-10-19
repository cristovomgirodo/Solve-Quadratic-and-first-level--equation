#
# The RealsComplexRoots.py module -- update in 20211019
# Developed by Cristovom A. Girodo
# 

import math
import cmath

def reals_complex_roots():
    
    # global variables
    a, b, c, delta, expression, raisedelta, root, root1, root2 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    
    def introduce():
        coef = eval(input("\t-_- What is the new value? "))
        return coef
    
    def enterData():
        for j in range(1, 4):
            if j == 1:
                print("\n\t* Provide the %dº" %j,"[coefficient].")
                u = introduce()
            elif j == 2:
                print("\n\t* Enter with the %dº" %j,"[coefficient].")
                v = introduce()
            elif j == 3:
                print("\n\t* Give the %dº" %j,"[coefficient].")
                w = introduce()
                return u, v, w    # local variables
          
    a, b, c = enterData()
    
    # here, update the code of the RealsComplexRoots.py module

    while a == 0 and b == 0 and c == 0:
        print('\n\n\t //////')
        print('\t(º < º) [ WARNING! ]')
        print('\t \ - /')
        print('\t** [ No exist none complete quadratic equation: [ a*x**2+b*x+c = 0 ] when the coefficients: a = 0, b = 0 and c = 0 and')
        print('\t     too none first level equation: [ b*x+c = 0 ] to solve--Ok! ]**')
        print('\t-- [ Enter with [New values] to the [ coefficients: a = ?, b = ? and c = ? ]--\n')
        a, b, c = enterData()
    
    def answer():
        print("\n   + The [roots] are: ","\n   + The first  root(root1)=",format(root1,"<10.2f"),"\n   + The second root(root2)=",format(root2,"<10.2f"))
        return
    
    def display_raisedelta():
        print("   + The value of the [raisedelta] = ",format(raisedelta,"<10.2f"))
        return
    
    def first_root(h, i, j):
        firt = (-i+j)/(2*h)
        return firt
    
    def second_root(h, i, j):
        secrt = (-i-j)/(2*h)
        return secrt

    print("\n\n\t\t============================================")
    print("\t\t| . . . *[ ANSWER TO THE EQUATION ]* . . . |")
    print("\t\t============================================\n")

    if a != 0 and b != 0 and c != 0:
        delta = b**2-4*a*c
        print("\n   + The new value of [delta] = ", delta)
        if delta > 0:
            raisedelta = math.sqrt(delta)
            view = display_raisedelta()
            p, q, r = a, b, raisedelta
            root1 = first_root(p, q, r)
            root2 = second_root(p, q, r)
            solution = answer()
            
        elif delta < 0:
            print("\n   --------------------------------------------------------------------")
            print("   * When the value of delta is negative the equation: a*x**2+b*x+c = 0\n\
            to theorem have not reals roots. *")
            print("   --------------------------------------------------------------------")
            print("\n\n\t   * Will get only two complexs roots *\n")
            raisedelta = cmath.sqrt(delta)
            view = display_raisedelta()
            p, q, r = a, b, raisedelta
            root1 = first_root(p, q, r)
            root2 = second_root(p, q, r)
            solution = answer()
            
        elif delta == 0:
            root1 = root2 = (-b+0.0)/(2*a)
            solution = answer()
            
    elif a > 0 and b == 0 and c > 0 or a < 0 and b == 0 and c < 0:
        print("\n  - The new equation of the second level geted will: [ a*x**2+c = 0 or\n\
    -a*x**2-c = 0 ] and will have two complexs roots.\n")
        expression = -((c + 0.0)/a)
        root1 = cmath.sqrt(expression)
        root2 = -cmath.sqrt(expression)
        print("\n   + The value of the expression:[ -c/a ] will:",format(expression,"<10.2f"))
        solution = answer()
        
    elif a < 0 and b == 0 and c > 0 or a > 0 and b == 0 and c < 0:
        print("\n  - The new equation of the second level geted will: [ -a*x**2+c = 0 or\n\
    a*x**2-c = 0 ] and will have two reals roots.\n")
        expression = -(c + 0.0)/a
        root1 = math.sqrt(expression)
        root2 = -math.sqrt(expression)
        print("\n   + The value of the expression: [ c/a ] will: ",format(expression,"<10.2f"))
        solution = answer()
        
    elif a > 0 and b > 0 and c == 0 or a < 0 and b < 0 and c == 0 or a < 0 and b > 0 and c == 0 or a > 0 and b < 0 and c == 0:
        print("\n  - The new equation of the second level geted will an of the followings:\n\
    [ a*x**2+b*x = 0 or -a*x**2-b*x = 0 or a*x**2-b*x = 0 or -a*x**2+b*x = 0 ]\n\
      and will have two reals roots.\n")
        root1 = 0
        root2 = -(b+0.0)/a
        solution = answer()
        
    elif a == 0 and b != 0 and c != 0:
        print("\n  - The new equation of the first level geted will: [ b*x+c = 0 ]\n    and will have an only real root.")
        if b > 0 and c > 0 or b < 0 and c < 0:
            root = (-c + 0.0) / b
        elif b > 0 and c < 0 or b < 0 and c > 0:
            root = (c + 0.0) / b
        
        print("\n\n\t+ The new real root will: ",format(root,"<10.2f"))

    print("\n\n  =====================================================================")
    print("  |º>º If necessary process the RealsComplexRoots.py module again! º>º|")
    print("  =====================================================================")


reals_complex_roots()





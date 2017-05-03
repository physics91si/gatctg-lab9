#!/usr/bin/python
import sys
import numbers
import numpy as np
#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    try:
        a = sys.argv[1]
        b = sys.argv[2]
        c = sys.argv[3]
        x1, x2 = find_roots(a, b, c)
        print ("This is x1: %f" %x1)
        print ("This is x2: %f" %x2)
    except:
        print("Please enter 3 numbers representing the polynomial coefficients") 
def find_roots(a,b=None,c=None, *extras):
    try:
        extraleng = len(extras)
        mid = b**2 - 4*a*c
        if int(extraleng) > 0:
            print("inside")
            raise SyntaxError("You entered in too many parameters")
        if a == 0:
            raise RuntimeError("Linear equation, not quadratic!")
        if mid < 0:
            raise myException("Function has imaginary roots")
        sqrt_mid = np.sqrt(mid)
        x1 = (-b + sqrt_mid)/(2*a)
        x2 = (-b - sqrt_mid)/(2*a)
        return x1, x2
    except TypeError:
        print("Please enter 3 numbers representing the polynomial coefficients")
    except NameError:
        print("Function has imaginary roots :)")
        return (None, None)
    except RuntimeError:
        print("You entered a linear equation, not a quadratic one")
    except SyntaxError:
        print("You entered in too many parameters")

if __name__=="__main__":
        main()

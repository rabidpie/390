# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import sqrt, log

def quadratic():
    """quadratic()
    Asks the user for the values of a, b, and c from the equation in the form 
    of ax^2+bx+c=0. The program will then check for possible answers based on
    the value of the discriminant, b^2-(4ac)."""
    a, b, c = input("enter the values for a, b, and c in that order:")
    d = b*b-(4*a*c)
    if d < 0:
        print "d is less than zero, no real solutions."
        return
    elif d == 0:
        x = -b/(2*a)
        print "d is zero, one real solution:" , x
        return
    else:
        x1 = (-b+sqrt(d))/(2*a)
        x2 = (-b-sqrt(d))/(2*a)
        print "d is greater and not equal to zero, two real solutions exist:" , x1, "and", x2

def calculateY(x):
    if (x > 1 or x == 1):
        print "The value of x must be less than 1 to take the ln(x)."
        return
    else:
        y = log(1/(1-x))
        return y

def SilentQuadratic(a, b, c):
    d = b*b-(4*a*c)
    FirstRoot = "No Value"
    SecondRoot = "No Value"
    if d < 0:
        NumberOfRealRoots = 0
    elif d == 0:
        FirstRoot = (-b)/(2*a)
        NumberOfRealRoots = 1
    else:
        FirstRoot = (-b+sqrt(d))/(2*a)
        SecondRoot = (-b-sqrt(d))/(2*a)
        NumberOfRealRoots = 2
    return NumberOfRealRoots, FirstRoot, SecondRoot

def Collision():
    a, b, c = input("Input deceleration, initial velocity, and initial distance:")
    t = (b - 0)/a
    y, t1, t2 = SilentQuadratic(0.5*a, b, -c)
    if t1 > t:
        print "Stopped before cat"
    elif t == t2:
        print "Close only counts in horse shoes and hand grendades, dead cat"
    else:
        if t1 < t:
            print "It took", t1, " odd seconds to hit the cat"
    return

def compare (num1, num2):
    if num1 > num2:
        return 1
    elif num1 == num2:
        return 0
    else:
        return -1


def isEven(num):
    if num%2 == 0:
        return True
    else:
        return False


def isOdd(num):
    if isEven(num) == True:
        return False
        
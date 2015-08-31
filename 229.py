#!/usr/bin/python3

import math
import random

def dottie(n):
        x = math.cos(n)
        y = math.cos(x)
        while( x != y ):
                x = y
                y = math.cos(y)
        print("dottie #: ", y)

def option1(n):
        x = n - math.tan(n)
        y = x - math.tan(x)
        while ( x != y ):
                x = y
                y = x - math.tan(x)
        print("option1 #:", y)

def option2(n):
        x = 1*n*(1/n)
        y = 1*x*(1/x)
        c = 0
        try:
                while ( x != y ):
                        x = y
                        y = 1*x*(1/x)
                        c = c + 1
                        if c > 500:
                                raise RuntimeError("{} doesn't converge".format(n))
                print("option2 #:", y)

        except RuntimeError as e:
                print(e)

def option3(n):
        x = 4*n*(1-n)
        y = 4*x*(1-x)
        c = 0
        try:
                while ( x != y ):
                        x = y
                        y = 4*x*(1-x)
                        c = c + 1
                        if c > 500:
                                err = "option3 #: {} doesn't converge".format(n)
                                raise RuntimeError(err)
                print("option3 #:", y)

        except RuntimeError as e:
                print(e)

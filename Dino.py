import math
import numpy as np
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.subsets import Subset
import sympy as sy

def NUM(int):
    print(int + int - int)

def BIN(int):
    print(bin(int))

def HEX(int):
    print(hex(int))

def OCT(int):
    print(oct(int))

def DC(int):
    print(hex(int+int*2))

def GHOST(int):
    print(bin(int + int - int * 100))

def RS(int):
    print(hex(int + int - int * 2 + int + int - int))

def OL(n1, n2, n3, n4):
    print((math.sqrt(n1 * n2 * n3 * n4 - (n1 * n4))))
    a = [n1, n2, n3, n4]
    print('your numbers:', a)

def PL(row1, row2):
    a = np.array([
        [row1, row2, row1 * row2]
    ])
    print('your row1 in bin:', bin(row1))
    print('your row2 in bin:', bin(row2))
    print('your rows array:', a)

class Cardinal:
    
    def cardinality(self):
        a1 = Subset([input("1:"), input("2:")], [input("1:"), input("2:"), input("3:"), input("4:"), input("5:")])
        print("Subset a cardinality : ", a1.cardinality)  
    
    def infintiy_except(self):
        a = int(input("n:"))
        b = sy.symbols(input("X:"))
        c = int(input("range:"))
        l = []
        for i in range(c):
            x = int(input("int:"))
            a1 = a * (a * a * a * a * a)
            a2 = a1 ** x * a1 ** x * (a1 * a1 * a1 * x)
            a3 = a2 * a1 ** x
            a4 = a3 * a3 ** x
            l.append(a4 * x * b)
            y = int(input("int2:"))
            infintiy_except = l * y
            print("infintiy except:", infintiy_except)

class factorial:
    def x_factorial(self):
        while True:
            a = int(input("Known:"))
            b = sy.symbols(input("Unknown:"))
            c = int(input("UT:"))
            d = b = a / c
            e = int(d)
            f = math.factorial(e)
            print("Unknown:", e)
            print("Factorial of Unknown:", f)

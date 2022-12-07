import math

import numpy as np

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

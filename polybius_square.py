#!/usr/bin/python2.7

import argparse,string
from random import randint

def get_polybius(mixed=False,omit='j'):
    """
    Produces a five by five polybius square, populated with
    lowercase letters. One letter must be omitted to fit 
    alphabet into the square. 
    Supports filling square with random, non-repeating letters.
    """
    alphabet = list(string.ascii_lowercase)
    alphabet.remove(omit)
    size = 5

    square = [[0 for i in range(size)] for i in range(size)]
    
    alpha_dex = 0
    for i in square:
        index = 0
        while index < size:
            if mixed:
                rand = randint(0,len(alphabet)-1)
                i[index] = alphabet[rand]
                del alphabet[rand]
            else:
                i[index] = alphabet[alpha_dex]
                alpha_dex += 1
            index += 1
    
    return square


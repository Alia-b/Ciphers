#!/usr/bin/python2.7

import string
from random import randint

def get_polybius(mixed=False,omit='j',alphabet=[]):
    """
    Returns a dicitionary with chars as keys mapped to their coordinates
    (y,x) in a five by five polybius square.
    Letters are mapped from  one to five, inclusive.

    Argument explanation:
        
        mixed:
            Boolean. If True the position of the letters will be randomized
            Defaults to False.
        omit:
            Char. The char to omit from the alphabet so it will cleanly fit
            into a 5 by 5 square. Defaults to 'j'. 
        alpha:
            List. The alphabet to use in the square. Be sure it has 26 chars
            and contains omit. Defaults to list(string.ascii_lowercase)
    
    """
    if not alphabet:
       alphabet = list(string.ascii_lowercase)
    alphabet.remove(omit)
    size = 5
    coords = {}

    for x in range(5,0,-1):
        for y in range(5,0,-1):
            if mixed:
                rand = randint(0,len(alphabet)-1)
                coords[alphabet[rand]] = (y,x)
                del alphabet[rand]
            else:
                coords[alphabet.pop()] = (x,y)
    return coords



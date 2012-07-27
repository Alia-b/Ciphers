#!/usr/bin/python2.7

import string
from random import randint

def get_polybius(key='',mixed=False,omit='j',switch='i',alphabet=[]):
    """
    Returns a dicitionary with chars as keys mapped to their coordinates
    (y,x) in a five by five polybius square.
    Letters are mapped from  one to five, inclusive.

    Argument explanation:
        key:
            The key to start the square with. The square is started  with the
            letters of the key and the remaining spaces are filled with the 
            rest of the alphabet that are not used by the key. Defaults to 
            the empty string. Optional.
        mixed:
            Boolean. If True the position of the letters will be randomized
            Defaults to False.
        omit:
            Char. The char to omit from the alphabet so it will cleanly fit
            into a 5 by 5 square. Defaults to 'j'. 
        switch:
            Char. Occurences of omit in key will be replaced with switch.
            Defaults to 'i'. If changing key or omit, switch must be changed
            or get_polybius will produce unexpected behavior.
        alpha:
            List. The alphabet to use in the square. Be sure it has 26 chars
            and contains omit. Defaults to list(string.ascii_lowercase)
    
    """
    if not alphabet:
       alphabet = list(string.ascii_lowercase)
    if key:
        key = list(key.replace(omit,switch))
        #Remove the letters of key from alphabet to avoid duplicates.
        for char in key:
            alphabet.remove(char)
    if omit in alphabet:
        alphabet.remove(omit)
    size = 5
    coords = {}
    
    for x in range(5,0,-1):
        for y in range(5,0,-1):
            if alphabet:
                if mixed:
                    rand = randint(0,len(alphabet)-1)
                    coords[alphabet[rand]] = (y,x)
                    del alphabet[rand]
                else:
                    coords[alphabet.pop()] = (x,y)
            else:
                coords[key.pop()] = (x,y)
    return coords



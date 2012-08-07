#!/usr/bin/python2.7

import string
from random import randint
from math import sqrt

def get_inverse(dict):
    '''Returns the inverse of the suplied dictionary'''
    inverse = {}
    for i in dict:
        inverse[dict[i]]=i
    return inverse

def remove_duplicates(string):
    out_string = []
    for i in string:
        if i not in out_string:
            out_string.append(i)
    return ''.join(out_string)

def get_polybius(key='',mixed=False,omit='j',switch='i',alphabet=[],inverse_map=False):
    """
    Returns a dicitionary with chars as keys mapped to their coordinates
    (y,x) in a polybius square.
    Letters are mapped from  zero to sqrt(len(alphabet+key)), inclusive.

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
            List. The alphabet to use in the square. Must be able to cleanly fit 
            into a square after removing omit.
            Defaults to list(string.ascii_lowercase)
        inverse_map:
            Boolean. If true also return the inverse dictionary (coordinates to letters)
    """
    if not alphabet:
       alphabet = list(string.ascii_lowercase)
    if key:
        key = remove_duplicates(key)
        key = list(key.replace(omit,switch))
        #Remove the letters of key from alphabet to avoid duplicates.
        for char in key:
            alphabet.remove(char)
    if omit in alphabet:
        alphabet.remove(omit)
   
    if not key:
        square_size = int(sqrt(len(alphabet)))
    else:
        square_size = int(sqrt(len(alphabet)+len(key)))

    coords = {}
    
    for x in range(square_size-1,-1,-1):
        for y in range(square_size-1,-1,-1):
            if alphabet:
                if mixed:
                    rand = randint(0,len(alphabet)-1)
                    coords[alphabet[rand]] = (y,x)
                    del alphabet[rand]
                else:
                    coords[alphabet.pop()] = (x,y)
            else:
                coords[key.pop()] = (x,y)
    if inverse_map:
        return coords, get_inverse(coords)
    else:
        return coords



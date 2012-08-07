#!/usr/bin/python2.7
import argparse
from polybius_square import get_polybius

def cipher(plain_text,letter_coords,in_letter_coords):
    """
    Rearrange the y,x coordinates of the plain_text on a 
    polybius square to a list of all y coordinates followed
    by all x coordinates.

    The first numbers of the list are then read off by twos
    and used as the y,x coords of the cipher letters. 
    """

    y_coords = []
    x_coords = []
    for i in plain_text:
        coords = letter_coords[i]
        y_coords.append(coords[0])
        x_coords.append(coords[1])

    complete = y_coords + x_coords
    cipher_text = []
    for i in range(0,len(complete),2):
       cipher_coords = (complete[i],complete[i+1])
       cipher_text.append(in_letter_coords[cipher_coords]) 
    
    return ''.join(cipher_text)

def decipher(cipher_text,letter_coords,in_letter_coords):

    complete =[]
    for i in cipher_text:
        coords = letter_coords[i]
        complete.append(coords[0])
        complete.append(coords[1])

    y = complete[:len(complete)/2]
    x = complete[len(complete)/2:]
        
    plain_text = []
    for i in range(len(y)):
        plain_coords= (y[i],x[i])
        plain_text.append(in_letter_coords[plain_coords])
    
    return ''.join(plain_text)

def create_cipher(args):
    
   
    if args.text:
        text = args.text.lower()
    elif args.file:
        text = open(args.file).read().lower()
    #Polybius square mappings.
    letter_map,inverse_letter_map = get_polybius(inverse_map=True)

    if args.decipher:
        return decipher(text,letter_map,inverse_letter_map).upper()
    else:
        return cipher(text,letter_map,inverse_letter_map).upper()


parser = argparse.ArgumentParser(description="A 5x5 bifid cipher")
parser.add_argument('--decipher','-d',help="Decipher the text",
                    action="store_true")
parser.add_argument('--text','-t',help="The text to work on.")
parser.add_argument('--file','-f',help="The file tow work on.")

parser.set_defaults(func=create_cipher)
args=parser.parse_args()
print args.func(args)

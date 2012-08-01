#!/usr/bin/python2.7
import argparse
from polybius_square import get_polybius
from digrams import get_digrams
from math import sqrt

def get_new_digram(in_digram,table,inverse_table,decipher):
    """
    Accepts a digram and returns a digram changed by the rules
    of the Playfair cipher.
    """

    if decipher:
        move = -1
    else:
        move = 1

    #The size of a side of the table for modulo divisions.
    #Used to keep moved letters cycling around the table.
    size = int(sqrt(len(table)))
    
    #Get the coordinates of the letters from the table
    a_coords = table[in_digram[0]]
    b_coords = table[in_digram[1]]

    if a_coords[0] == b_coords[0]:
        #Letters in the same row
        cipher_a = ((a_coords[0],(a_coords[1]+move)%size))
        cipher_b = ((b_coords[0],(b_coords[1]+move)%size))
    elif a_coords[1] == b_coords[1]:
        #Letters in same column
        cipher_a = (((a_coords[0]+move)%size,a_coords[1]))
        cipher_b = (((b_coords[0]+move)%size,b_coords[1]))
    else:
        #Letter coords form rectangle
        cipher_a = ((a_coords[0],b_coords[1]))
        cipher_b = ((b_coords[0],a_coords[1]))
    
    #inverse_table looks up the letter from the coordinatess
    out_digram =[inverse_table[cipher_a],inverse_table[cipher_b]]
    
    return out_digram



def create_cipher(args):
    """
    Cipher things in a specified way.
    """
    if args.text:
        text = args.text
    elif args.file:
        text = open(args.file).read()
 
    digrams = get_digrams(list(text),'x') 

    out_text = []

    table = get_polybius(key=args.pass_phrase)
    #Creates an inverse table for lookups
    in_table = {}
    for i in table:
        in_table[table[i]] = i
    
    for i in digrams:
        out_text += get_new_digram(i,table,in_table,args.decipher)

    return ''.join(out_text)

parser = argparse.ArgumentParser(description="The Playfair Cipher")
parser.add_argument('--cipher','-c',help="Cipher the text",
                    action="store_true")
parser.add_argument('--decipher','-d',help="Decipher the text",
                    action="store_true")
parser.add_argument('--text','-t',help="The text to work on.")
parser.add_argument('--file','-f',help="The file to work on.")
parser.add_argument('pass_phrase',help="The pass-phrase to use.")

parser.set_defaults(func=create_cipher)
args=parser.parse_args()
print args.func(args)

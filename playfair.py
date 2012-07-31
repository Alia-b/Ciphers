#!/usr/bin/python2.7
import argparse
from polybius_square import get_polybius
from digrams import get_digrams

def get_new_digram(in_digram,decipher):
    
    table = get_polybius(key=args.pass_phrase)
    #Creates an inverse table for lookups
    in_table = {}
    for i in table:
        in_table[table[i]] = i
    if decipher:
        move = -1
    else:
        move = 1

    #The size of the table for modulu.
    mod = 5
    
    a_coords = table[in_digram[0]]
    b_coords = table[in_digram[1]]

    if a_coords[0] == b_coords[0]:
        #Letters in the same row
        cipher_a = ((a_coords[0],(a_coords[1]+move)%mod))
        cipher_b = ((b_coords[0],(b_coords[1]+move)%mod))
    elif a_coords[1] == b_coords[1]:
        #Letters in same column
        cipher_a = (((a_coords[0]+move)%mod,a_coords[1]))
        cipher_b = (((b_coords[0]+move)%mod,b_coords[1]))
    else:
        #Letter coords form rectangle
        cipher_a = ((a_coords[0],b_coords[1]))
        cipher_b = ((b_coords[0],a_coords[1]))
    
    out_digram =[]
    out_digram.append(in_table[cipher_a])
    out_digram.append(in_table[cipher_b])
    return out_digram

def cipher(digrams,decipher):
    out_text = []

    for i in digrams:
        out_text += get_new_digram(i,decipher)
    
    return ''.join(out_text)
            



def create_cipher(args):
    """
    Cipher things in a specified way.
    """
    if args.text:
        text = args.text
    elif args.file:
        text = open(args.file).read()

    
    digrams = get_digrams(list(text),'x')

    return cipher(digrams,args.decipher)

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

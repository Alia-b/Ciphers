#!/usr/bin/python2.7
import argparse
from polybius_square import get_polybius
from digrams import get_digrams

def substitute(text,right_key,left_key,decipher):

    #Get the mappings for polybius squares and their inverse
    #The inverse is for lookups.
    plain_table,in_plain = get_polybius(inverse_map=True)
    right_table,in_right = get_polybius(key=right_key,
                                        inverse_map=True)
    left_table,in_left = get_polybius(key=left_key,
                                        inverse_map=True)
    
    #Get the digrams for the text as a list of tuples.
    text = get_digrams(list(text),allow_doubles=True)
    
    out_text = []
    for i in text:
        if not decipher:
            a_coords = plain_table[i[0]]
            b_coords = plain_table[i[1]]
         
            out_text.append(in_right[(a_coords[0],b_coords[1])])
            out_text.append(in_left[(b_coords[0],a_coords[1])])
        else:
            a_coords = right_table[i[0]]
            b_coords = left_table[i[1]]

            out_text.append(in_plain[(a_coords[0],b_coords[1])])
            out_text.append(in_plain[(b_coords[0],a_coords[1])])

    return ''.join(out_text).upper()

    
def create_cipher(args):
    """
    A four square polygraphic substitution cipher.

    """
    if args.text:
        text = args.text.lower()
    elif args.file:
        text = open(args.file).read().lower()
    
    return substitute(text,args.right_key,args.left_key,args.decipher)


parser = argparse.ArgumentParser(description="A four square cipher")
parser.add_argument('--decipher','-d',help="Decipher the text",
                    action="store_true")
parser.add_argument('--text','-t',help="The text to work on.")
parser.add_argument('--file','-f',help="The file to work on.")
parser.add_argument('right_key',help="The key for the bottom left square.")
parser.add_argument('left_key',help="The key for the top right square.")

parser.set_defaults(func=create_cipher)
args=parser.parse_args()
print args.func(args)

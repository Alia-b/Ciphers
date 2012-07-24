#!/usr/bin/python2.7
import argparse
from itertools import chain

def transpose(text,key):
    cipher_table  = []
    
    for i in key:
        cipher_table.append([i,[]])

    position = 0
    for i in text:
        cipher_table[position][1].append(i)
        position = (position + 1)%len(cipher_table)

    sorted_key = list(key)
    sorted_key.sort()
    
    cipher_lists = []

    for i in sorted_key:
        for k in range(len(cipher_table)):
            if cipher_table[k][0] == i and cipher_table[k][1] not in cipher_lists:
                cipher_lists.append(cipher_table[k][1])
    
    flattened = chain.from_iterable(cipher_lists)
    return ''.join(list(flattened))

def decipher(cipher_text,key):
    pass

def create_cipher(args):
    """
    Cipher things in a specified way.
    """
    text = args.text.upper()
    key = args.key.upper()
    if args.cipher:
        return transpose(text,key)
    elif args.decipher:
        return decipher(text,key)


parser = argparse.ArgumentParser(description="A cipher")
parser.add_argument('--cipher','-c',help="Cipher the text",
                    action="store_true")
parser.add_argument('--decipher','-d',help="Decipher the text",
                    action="store_true")
parser.add_argument('text',help="The text to work on.")
parser.add_argument('key',help="The key to use.")

parser.set_defaults(func=create_cipher)
args=parser.parse_args()
print args.func(args)

#!/usr/bin/python2.7
import argparse
from itertools import chain

def get_table(text,key):
    cipher_table  = []
    
    for i in key:
        cipher_table.append([i,[]])

    position = 0
    for i in text:
        cipher_table[position][1].append(i)
        position = (position + 1)%len(cipher_table)
    
    return cipher_table

def transpose(text,key):
    
    sorted_key = sorted(key)
    cipher_table = get_table(text,key)
    cipher_lists = []

    for i in sorted_key:
        for k in range(len(cipher_table)):
            if cipher_table[k][0] == i and cipher_table[k][1] not in cipher_lists:
                cipher_lists.append(cipher_table[k][1])
    
    flattened = chain.from_iterable(cipher_lists)
    return ''.join(list(flattened))

def decipher(cipher_text,key):
    table = get_table(cipher_text,key)
    sorted_key = sorted(key) 
    
    ordered_table = []
    pos = 0
    for letter in sorted_key:
        for i in range(len(table)):
            if table[i][0] == letter and table[i] not in ordered_table :
                for k in range(len(table[i][1])):
                    table[i][1][k] = cipher_text[pos]
                    pos +=1
                ordered_table.append(table[i])
    
    
    restored_table = []
    for i in key:
        for k in ordered_table:
            if k[0] == i and k[1] not in restored_table:
                restored_table.append(k[1])
                break 
    
    plain_text = []
    place = 0
    while place < len(restored_table[0]):
        for entry in restored_table:
            if place < len(entry):
                plain_text.append(entry[place])
        place += 1

    return ''.join(plain_text)


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

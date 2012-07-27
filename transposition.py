#!/usr/bin/python2.7
import argparse
from itertools import chain

def get_table(text,key):
    """
    Creates and returns the table used for ciphering.

    Example:
    
    key = farce
    text = MeetAtNoonByTheWesternGate 
    
    cipher_table =
    ['F', ['M', 'T', 'B', 'W', 'R', 'E']]
    ['A', ['E', 'N', 'Y', 'E', 'N']]
    ['R', ['E', 'O', 'T', 'S', 'G']]
    ['C', ['T', 'O', 'H', 'T', 'A']]
    ['E', ['A', 'N', 'E', 'E', 'T']]
    """
    cipher_table  = []
    
    for i in key:
        cipher_table.append([i,[]])

    position = 0
    for i in text:
        cipher_table[position][1].append(i)
        position = (position + 1)%len(cipher_table)
    
    for i in cipher_table:
        print i
    return cipher_table

def transpose(text,key):
    '''
    Transposes the text.
    '''

    sorted_key = sorted(key)
    cipher_table = get_table(text,key)
    cipher_lists = []
    
    #Grabs the char lists from table in the specified order and resorts
    #them to alphabetical by key order. 
    for i in sorted_key:
        for k in range(len(cipher_table)):
            if cipher_table[k][0] == i and cipher_table[k][1] not in cipher_lists:
                cipher_lists.append(cipher_table[k][1])
    
    flattened = chain.from_iterable(cipher_lists)
    return ''.join(list(flattened))

def decipher(cipher_text,key):
    '''
    Deciphers the text.
    '''
    #The letter order in the table is useless, but the dimensions are
    #identical to the table used to cipher the text. Consider it 
    #filled with nulls.. 
    table = get_table(cipher_text,key)
    sorted_key = sorted(key) 
    
    #Creates an ordered table with the rows in sorted order.
    ordered_table = []
    pos = 0
    for letter in sorted_key:
        for i in range(len(table)):
            if table[i][0] == letter and table[i] not in ordered_table :
                for k in range(len(table[i][1])):
                    table[i][1][k] = cipher_text[pos]
                    pos +=1
                ordered_table.append(table[i])
    
    #Restored_table is identical to the table created during ciphering
    #with get_table(text,key)
    restored_table = []
    for i in key:
        for k in ordered_table:
            if k[0] == i and k[1] not in restored_table:
                restored_table.append(k[1])
                break 

    #Extracts the text from restored_table
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

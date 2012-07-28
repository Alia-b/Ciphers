#!/usr/bin/python2.7
import argparse
import string

def get_sub_map(from_alphabet,to_alphabet):
    '''
    Creates the dictionary for substitution lookup.
    Uses from_alphabet as keys and to_alphabet as values
    '''
    sub_map = {}
    for i in range(len(from_alphabet)):
        sub_map[from_alphabet[i]] = to_alphabet[i]
    
    return sub_map

def substitute(in_text,substitution_map):
        out_text = []
        for i in in_text:
            if i not in substitution_map:
                out_text.append(i)
            else:
                out_text.append(substitution_map[i])

        return ''.join(out_text)

def create_cipher(args):
    """
    A simple monoalphabetic substitution cipher with a user-supplied
    alphabet.

    Note that we are only working with letters so the supplied 
    alphabet must be 26 characters long.
    """
    if args.text:
        in_text = args.text.upper()        
    elif args.file:
        in_text =  open(args.file).read().upper()
    
    if args.cipher:
        sub_map = get_sub_map(string.ascii_uppercase,args.alphabet)
    elif args.decipher:
        sub_map = get_sub_map(args.alphabet,string.ascii_uppercase)

    return substitute(in_text,sub_map)
    


parser = argparse.ArgumentParser(description="A cipher")
parser.add_argument('--cipher','-c',help="Cipher the text",
                    action="store_true")
parser.add_argument('--decipher','-d',help="Decipher the text",
                    action="store_true")
parser.add_argument('--text','-t',help="The text to work on.")
parser.add_argument('--file','-f',help="The file to work on.")
parser.add_argument('alphabet',help="The substitution alphabet to use.")

parser.set_defaults(func=create_cipher)
args=parser.parse_args()
print args.func(args)

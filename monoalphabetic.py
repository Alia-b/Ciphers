#!/usr/bin/python2.7
import argparse
import string

def create_cipher(args):
    """
    A simple monoalphabetic substitution cipher with a user-supplied
    alphabet.

    Note that we are only working with letters so the supplied 
    alphabet must be 26 characters long.
    """
    alphabet = list(args.alphabet.upper())
    if args.cipher:
        plain_text = args.text.upper()
        
        substitution_map = {}
        for i in string.ascii_uppercase:
            substitution_map[i] = alphabet[0]
            del alphabet[0]

        cipher_text = []
        for i in plain_text:
            cipher_text.append(substitution_map[i])

        return ''.join(cipher_text)
    
    elif args.decipher:
        cipher_text = args.text.upper()

        substitution_map = {}
        plain_alphabet = list(string.ascii_uppercase)
        for i in alphabet:
            substitution_map[i] = plain_alphabet[0]
            del plain_alphabet[0]
        
        plain_text = []
        for i in cipher_text:
            plain_text.append(substitution_map[i])

        return ''.join(plain_text)


parser = argparse.ArgumentParser(description="A cipher")
parser.add_argument('--cipher','-c',help="Cipher the text",
                    action="store_true")
parser.add_argument('--decipher','-d',help="Decipher the text",
                    action="store_true")
parser.add_argument('text',help="The text to work on.")
parser.add_argument('alphabet',help="The substitution alphabet to use.")

parser.set_defaults(func=create_cipher)
args=parser.parse_args()
print args.func(args)

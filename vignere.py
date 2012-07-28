#!/usr/bin/python2.7
import argparse
import string

def get_letter_maps():
    letter_map = {}
    inverse_letter_map = {}

    value = 0
    for i in string.ascii_uppercase:
        letter_map[i] = value
        inverse_letter_map[value] = i
        value += 1
    
    return letter_map,inverse_letter_map

def get_key(key_seed,length):
    key = []

    pos = 0
    while len(key) != length:
        key.append(key_seed[pos%len(key_seed]))
        pos += 1
    return key

def create_cipher(args):
    """
    Cipher things in a specified way.
    """
    if args.text:
        text = args.text.upper()
    elif args.file:
        text = open(args.file).read().upper()

    let_map,in_let_map = get_letter_maps()

    key = get_key(args.key,len(text))





parser = argparse.ArgumentParser(description="A cipher")
parser.add_argument('--cipher','-c',help="Cipher the text",
                    action="store_true")
parser.add_argument('--decipher','-d',help="Decipher the text",
                    action="store_true")
parser.add_argument('--text','-t',help="The text to work on.")
parser.add_argument('--file','-f',help="The file to work on.")
parser.add_argument('key',help="The key to use.")

parser.set_defaults(func=create_cipher)
args=parser.parse_args()
print args.func(args)

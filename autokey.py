#!/usr/bin/python2.7
import argparse
import string

def create_cipher(args):
    """
    """
    key = list(args.key.upper())
    text = list(args.text.upper())
    letter_map = {}
    inverse_letter_map = {}
    print key
    print text
    value = 0
    for i in string.ascii_uppercase:
        letter_map[i] = value
        value += 1

    for i in letter_map:
        inverse_letter_map[letter_map[i]] = i

    if args.cipher:
        plain_text = text
        key = key + text[:len(text)-len(key)]
        cipher = []

        for i in range(len(plain_text)):
            plain_value = letter_map[plain_text[i]]
            key_value = letter_map[key[i]]
            cipher.append(inverse_letter_map[(plain_value+key_value)%26])

        return ''.join(cipher)
    elif args.decipher:
        
        cipher_text = text
        plain_text = []

        for i in range(len(cipher_text)):
            cipher_value = letter_map[cipher_text[i]]
            key_value = letter_map[key[i]]
            decipher_letter = inverse_letter_map[(cipher_value-key_value)%26]
            plain_text.append(decipher_letter)
            if len(key) < len(cipher_text):
                key.append(decipher_letter)
        
        return ''.join(plain_text)



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

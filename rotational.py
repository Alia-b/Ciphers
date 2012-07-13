#!/usr/bin/python2.7
import argparse

def rot(args):
    text = args.text
    rot = args.rot

    text_list = list(text)
    rot_list=[]

    for char in text_list:
        i = ord(char)

        if i in range(97,123):
            i = ((i - 97 + rot)%26)+97

        elif i in range(65,91):
            i = ((i - 65 + rot)%26)+65
        
        rot_list.append(chr(i))
    
    return "".join(rot_list)


parser = argparse.ArgumentParser(description="Simple rotational cipher")
parser.add_argument('text',help="The text to be ciphered")
parser.add_argument('--rot',type=int,nargs='?',default=13,
                    help="The number of letters to rotate. Default 13")
parser.set_defaults(func=rot)

args=parser.parse_args()
print args.func(args)

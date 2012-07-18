#!/usr/bin/python2.7

import argparse

from polybius_square import get_polybius

def create_cipher(args):
    mapping = get_polybius()
    text = args.text
    #The coordinates of the letters in order
    letter_coords =[]
    for i in text:
        letter_coords.append(mapping.get(i))
    
    transposed = []
    
    if args.cipher: 
        y=[]
        x=[]

        for i in letter_coords:
            y.append(i[0])
            x.append(i[1])
        complete = y + x
        
        for i in range(0,len(complete),2):
            transposed.append( (complete[i],complete[i+1])) 

    elif args.decipher:
        temp = []
        for i in letter_coords:
            temp.append(i[0])
            temp.append(i[1])
        y = temp[:len(temp)/2]
        x = temp[len(temp)/2:]
        
        for i in range(len(y)):
            transposed.append((y[i],x[i]))

    fin_text = []
    for i in transposed:
        for k in mapping:
            if mapping[k] == i:
                fin_text.append(k)
     
    return ''.join(fin_text)

parser = argparse.ArgumentParser(description="A 5x5 bifid cipher")
parser.add_argument('--cipher','-c',help="Cipher the text",action="store_true")
parser.add_argument('--decipher','-d',help="Decipher the text",action="store_true")
parser.add_argument('text',help="The text to work on.")

parser.set_defaults(func=create_cipher)
args=parser.parse_args()
print args.func(args)

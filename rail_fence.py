#!/usr/bin/python2.7

import argparse

def get_cipher(matrix):
    '''
    Extracts the cipher text from the matrix
    produced by rail_cipher
    '''

    cipher_text = []
    
    for row in matrix:
        for i in row:
            if i != 0:
                cipher_text.append(i)
    return ''.join(cipher_text)

def get_plain_text(matrix,cipher_text):
    '''
    By creating a matrix for the cipher-text
    we can produce an identically sized matrix
    as was used for the original ciphering. This
    also gives us the number of letters in each row
    and the coordinates of all the original letters.

    With a cipher-text of 'sietabsna' and a key of
    four we can deduce that the first row contained
    two letters at coordinates 0 and 6. Thus we can
    recreate the first row of the original cipher.
    [s,-,-,-,-,-,i,-,-]
    '''

    letter_coords =[]
    x_pos = 0
    y_pos = 0

    while y_pos < len(matrix): 
        while x_pos < len(matrix[y_pos]):
            if matrix[y_pos][x_pos] != 0:
                #Found a letter
                #Mark coordinates, and increment 
                #letters_in_row for this row.
                letter_coords.append([y_pos,x_pos])
            x_pos +=1
        x_pos = 0
        y_pos += 1
    #It's important to note that the coordinates in
    #letter_coords are in the same order as the 
    #letters in the cipher

    #Since the matrix is mutable, we'll just
    #change it in-situ rather than create another.
    cipher_list = list(cipher_text)
    tracker = 0
    for coord in letter_coords:
        matrix[coord[0]][coord[1]] = cipher_list[tracker]
        tracker += 1
    #Matrix is now identical to the original matrix
    #used in the original cipher
    
    clear_text = []
    xpos = 0
    ypos = 0
    yup = False
    for i in range(len(matrix[0])):
        clear_text.append(matrix[ypos][xpos])

        xpos += 1

        if ypos + 1 >= len(matrix):
            yup = True
        elif ypos - 1 < 0:
            yup = False

        if yup:
            ypos -= 1
        else:
            ypos +=1
    return ''.join(clear_text)

def rail_cipher(args):
    '''
    Creates the picket fence matrix and inserts to clear text
    into it.
    As python is not okay with empty list spaces, 'empty' 
    spaces are represented by the int 0.
    '''
    text = args.text
    key = int(args.key)
    decipher = False
    if args.decipher:
        decipher = True
    matrix = [ [ 0 for i in range(len(text)) ] for j in range(key) ]

    xpos = 0
    ypos = 0
    yup = False

    for char in text:
        matrix[ypos][xpos] = char

        xpos += 1

        if ypos + 1 >= key:
            yup = True
        elif ypos - 1 < 0:
            yup = False

        if yup:
            ypos -= 1
        else:
            ypos +=1

    if decipher:
        print get_plain_text(matrix,text)
    else:
        print  get_cipher(matrix)
    

parser = argparse.ArgumentParser(description="Simple rail fence cipher")
parser.add_argument('text',help="Text to be ciphered")
parser.add_argument('key',help="Key int")
parser.add_argument('--decipher',help="Instead of ciphering the text, decipher it",
                    action="store_true")
parser.set_defaults(func=rail_cipher)

args = parser.parse_args()
args.func(args)


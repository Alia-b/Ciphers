import warnings

def get_digrams(text,null='x'):
    """
    Returns a list of digrams for text.

    Odd length texts are padded by a null.

    Repeating characters are separated by a null
    
    Warns if the text contains the chosen null as this will likely
    cause an infinite loop of separating nulls with nulls.
    """
    if null in text:
        warnings.warn(
        "Text contains null. This could cause an infinite loop."
            )
    
    while True:
        '''
        Adds null between all repeating characters.
        '''
        for i in range(len(text)-1):
            if text[i] == text[i+1]:
                text = text[:i+1] + list(null) +text[i+1:]
                break 
        else:
            break
    if len(text) % 2 != 0:
        text.append(null)
    
    digrams = []
    for i in range(0,len(text),2):
        digrams.append((text[i],text[i+1]))


    return digrams

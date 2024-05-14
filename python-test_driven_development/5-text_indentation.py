#!/usr/bin/python3
"""Prints a text with 2 new lines after each of these characters: . ? and :"""

def text_indentation(text):
    """text must be a string, no space at the beginning or end of each line"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        ntx = text
        for i in range(len(text)):
            ntx = ntx.replace(". ", ".", 1)
            ntx = ntx.replace("? ", "?", 1)
            ntx = ntx.replace(": ", ":", 1)
        for j in range(len(ntx)):
            if ntx[j - 1] != "." and ntx[j - 1] != "?" and ntx[j - 1] != ":":
                print("{}".format(ntx[j]), end="")
            else:
                print("\n\n{}".format(ntx[j]), end="")

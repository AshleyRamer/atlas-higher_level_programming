#!/usr/bin/python3
"""2-append_write"""

def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns the number of chars created"""
with open(filename, mode='a', encoding="utf-8") as f:
    return f.write(text)

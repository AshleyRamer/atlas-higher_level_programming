#!/usr/bin/python3
""" 0-read_file """


def read_file(filename=""):
    """ function to read and print a file to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

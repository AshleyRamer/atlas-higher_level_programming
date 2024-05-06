#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 2:
        print("1 argument:")
        print(f"1: {argv[1]}")
    elif len(argv) == 1:
        print("0 arguments.")
    else:
        print(f"{len(argv) - 1} arguments:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")

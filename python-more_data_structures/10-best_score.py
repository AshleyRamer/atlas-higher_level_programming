#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = 0
        for x, y in a_dictionary.items():
            if y > best_score:
                best_key = x
                best_score = y
        return best_key
    else:
        return None

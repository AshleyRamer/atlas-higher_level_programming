#!/usr/bin/python3
def add_tuple(tup_a=(), tup_b=()):

    if len(tup_a) < 2:
        tup_a = tup_a + (0, 0)
    if len(tup_b) < 2:
        tup_b = tup_b + (0, 0)

    new_tup = (tup_a[0] + tup_b[0], tup_a[1] + tup_b[1])
    return new_tup

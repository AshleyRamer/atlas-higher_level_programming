#!/usr/bin/python3
"""3-to_json_string"""


import json


def to_json_string(my_obj):
    """Returns JSOed N representation of an object"""
    return json.dumps(my_obj)

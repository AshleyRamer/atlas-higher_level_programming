#!/urs/bin/python3
"""8-class_to_json"""

def class_to_json(obj):
    """Returns the dictionary definition with simple data struct for JSON serialization of an object."""
    return vars(obj)

""" name_function.py   : create a name -for unit test """

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}".title()
    else:
        full_name = f"{first} {last}".title()
    
    return full_name

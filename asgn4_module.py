"""
This module contains functions for completing
and satisfying requirements for assignment 4
in this Python class.
"""



def is_field_blank(string):
    """
    accepts a string from user input
    returns a boolean value to input prompt loop
    """
    if len(string) == 0:
        return True
    else:
        return False


def is_field_a_number(number):
    """
    accepts a number from user input
    returns a boolean value to input prompt loop
    """
    if number.isdigit():
        return True
    else:
        return False
    

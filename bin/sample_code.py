"""
MODULE
"""

import math

def calculate_hypotenuse(a, b):
    """
    FUNCTION DOCSTRING
    THIS IS A FUNCTION THAT CALCULATES THE HYPOTENUSE OF A RIGHT TRIANGLE GIVEN ITS TWO SIDES
    
    INPUTS
    
    a    integer, first side of the triangle
    b    integer, second side of the triangle
    
    OUTPUT
    
    hypotenuse    float, hypotenuse of the triangle
    """
    assert isinstance(a, int), f"expected int but got {type(a)}"
    assert isinstance(b, int), f"expected int but got {type(b)}"
    assert a>0, "side length of a triangle has to be bigger than zero!"
    assert b>0, "side length of a triangle has to be bigger than zero!"

    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

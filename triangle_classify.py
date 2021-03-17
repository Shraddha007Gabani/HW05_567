# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(a_first, b_second, c_third):
    """Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code"""

    # require that the input values be >= 0 and <= 200

    # require that the input values be >= 0 and <= 200
    if a_first > (200 or 0) or b_second > (200 or 0) or c_third > (200 or 0):
        return 'InvalidInput'
    if (a_first >= (b_second + c_third)) or\
            (b_second >= (a_first + c_third)) or\
            (c_third >= (a_first + b_second)):
        return 'NotATriangle'
# now we know that we have a valid triangle
    if a_first==b_second and b_second==c_third:
        return 'Equilateral'
    if (a_first*a_first + b_second*b_second == c_third*c_third)\
            or ( a_first*a_first + c_third*c_third == b_second*b_second) \
            or (b_second*b_second + c_third*c_third == a_first*a_first):
        return 'Right'
    if (a_first!=b_second) and (b_second!=c_third) and (c_third!=a_first):
        return 'Scalene'

    return 'Isoceles'

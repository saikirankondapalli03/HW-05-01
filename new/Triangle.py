'''
@author Sai
File name: HW-01.py
Date created: 1/28/2020
Date last modified: 1/28/2020
Python Version: 3.1
This program takes measurements of 3 sides and displays whether it is
side_1) Isosceles  side_2) Equilateral side_3) Right Triangle d) Scalene
'''


from numbers import Number


def classify_triangle(side_1, side_2, side_3):
    '''
    this function takes 3 sides as input.validates all 3 sides and check if it is triangle or not.
    '''
    if not isinstance(
            side_1,
            Number) or not isinstance(
                side_2,
                Number) or not isinstance(
                    side_3,
                    Number):
        return 'invalid input'
    if side_1 <= 0 | side_2 <= 0 | side_3 <= 0:
        return 'invalid input'
    if side_1 + side_2 <= side_3 or side_2 + side_1 <= side_3 or side_1 + side_3 <= side_2:
        return 'invalid input'
    if side_1 == side_2 and side_1 == side_3:
        return 'Equilateral triangle'
    if (side_1 == side_2 and side_1 != side_3) or (side_2 == side_3 and side_2 != side_1) or (side_3 == side_1 and side_3 != side_2):
        return 'Isoceles triangle'
    if side_1**2 + side_2**2 == side_3**2 or side_1**2 + side_3**2 == side_2**2 or side_2**2 + side_3**2 == side_1**2:
        return 'Right angled triangle'
    if side_1 != side_2 and side_2 != side_3 and side_3 != side_1:
        return 'Scalene triangle'

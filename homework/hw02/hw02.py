"""Homework 2."""

# Question 1

def harmonic_mean(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic_mean(2, 6)
    3.0
    >>> harmonic_mean(1, 1)
    1.0
    >>> harmonic_mean(2.5, 7.5)
    3.75
    >>> harmonic_mean(4, 12)
    6.0
    """
    return (2/(1/x+1/y))


# Question 2

def speed_converter(miles_per_min):
    """
    >>> speed_converter(0)
    0.0
    >>> speed_converter(0.5)
    1158.48
    >>> speed_converter(0.75)
    1737.72
    >>> speed_converter(2)
    4633.92
    """
    kilos_per_day =miles_per_min*1.609*24*60
    
    return kilos_per_day


# Question 3

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max(a*a+b*b, a*a+c*c, b*b+c*c)


# Question 4

def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """
    factor = n - 1
    while factor > 0:
        if (n*n-1) % factor == 0:
            return factor
        factor -= 1   

# Question 5

from math import sin

def law_of_sines(a, b, c, A, B, C):
    """
    >>> law_of_sines(1, 1, 1, 1.0472, 1.0472, 1.0472)
    True
    >>> law_of_sines(1, 2, 3, 1, 2, 3)
    False
    """
    is_triangle=(sin(A) / a == sin(B) / b) and (sin(B) / b == sin(C) / c)
    return is_triangle


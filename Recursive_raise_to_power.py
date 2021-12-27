# Problem statement
# Write a method that raises a number base to power of exponent recursively 
# without using the ^ operator or Math power utilities. The exponent can be negative.

def better_pow(base, exponent):
    """
    Recursively raises base to exponent and returns
    the result.
    :param base: The base.
    :param exponent: The power the base should be raised to.
    :return: Result of `base ^ exponent`.
    """
    #base case
    if exponent == 0:
      return 1.0
    #flip sign and continue with fraction
    if exponent < 0:
      return better_pow(1/base, -exponent)
    #shortcut even exponents 
    if exponent % 2 == 0:
      return better_pow(base * base, exponent/2)
    #otherwise normal recursion  
    else:
      return base * better_pow(base, exponent-1)

better_pow(-3,3)

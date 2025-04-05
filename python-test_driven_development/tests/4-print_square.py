>>> print_square = __import__('4-print_square').print_square

>>> print_square(4)
####
####
####
####

>>> print_square(-4)
Traceback (most recent call last):
ValueError: size must be >= 0

>>> print_square("4")
Traceback (most recent call last):
TypeError: size must be an integer

>>> print_square()
Traceback (most recent call last):
TypeError: print_square() missing 1 required positional argument: 'size'

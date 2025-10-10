"""
EXAMPLE MODULE
DISCARD THIS FOR YOUR PROJECT AND CREATE YOUR OWN MODULES ACCORDING TO YOUR NEEDS

This module performs operations execution, including printing names
formatted and the sum of numbers. It imports module-specific functions
external and displays results using provided settings.

Author: Filipe de Souza Martins
Date: January 27, 2024
"""

from settings.settings import name

from src.module1.module1 import (
    print_capitalized_name,
    print_lower_name,
    print_upper_name,
)
from src.module2.module2 import sum_numbers

if name is not None:
    print('Your name is: ', name)
    print(print_lower_name(name))
    print(print_upper_name(name))
    print(print_capitalized_name(name))
else:
    print('Name is None')

print(sum_numbers('R$2.500', 'R$2.500'))
print(sum_numbers('R$ 2.500', 'R$ 2.500'))
print(sum_numbers('USD2.500', 'USD 2.500'))
print(sum_numbers('2.500', 'R$2500'))
print(sum_numbers('2500', '2.500'))

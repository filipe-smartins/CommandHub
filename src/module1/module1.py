"""
EXAMPLE MODULE
DISCARD THIS FOR YOUR PROJECT AND CREATE YOUR OWN MODULES ACCORDING TO YOUR NEEDS

This module provides functions that modify the form of your name to print it on the screen.

Author: Filipe de Souza Martins
Date: January 27, 2024
"""

from settings.settings import name
from utils.utils import capitalized_name, lower_name, upper_name

from src.logger import logger


def print_lower_name(name_to_print: str) -> str:
    """
    Print the lowercase version of a given name.

    Parameters:
    - name_to_print (str): The name to print in lowercase.

    Returns:
    - str: A formatted string indicating the lowercase version of the input name.
    """
    logger.info(f'Starting print_lower_name with name {name_to_print}')

    result = lower_name(name_to_print)

    logger.info(f'Function generated the following result: {result}')

    return f'Your lower name is: {result}'


def print_upper_name(name_to_print: str) -> str:
    """
    Print the uppercase version of a given name.

    Parameters:
    - name_to_print (str): The name to print in uppercase.

    Returns:
    - str: A formatted string indicating the uppercase version of the input name.
    """

    logger.info(f'Starting print_upper_name with name {name_to_print}')

    result = upper_name(name_to_print)

    logger.info(f'Function generated the following result: {result}')

    return f'Your upper name is: {result}'


def print_capitalized_name(name_to_print: str) -> str:
    """
    Print the capitalized version of a given name.

    Parameters:
    - name_to_print (str): The name to print in capitalized form.

    Returns:
    - str: A formatted string indicating the capitalized version of the input name.
    """

    logger.info(f'Starting print_capitalized_name with name {name_to_print}')

    result = capitalized_name(name_to_print)

    logger.info(f'Function generated the following result: {result}')

    return f'Your capitalized name is: {result}'


if __name__ == '__main__':

    if name is not None:
        print(name)
        print(print_lower_name(name))
        print(print_upper_name(name))
        print(print_capitalized_name(name))
    else:
        print('Name is None')

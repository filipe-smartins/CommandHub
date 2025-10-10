"""
EXAMPLE MODULE
DISCARD THIS FOR YOUR PROJECT AND CREATE YOUR OWN MODULES ACCORDING TO YOUR NEEDS

This module provides functions for formatting names and converting numeric strings to
formatted numbers.

Author: Filipe de Souza Martins
Date: January 27, 2024
"""


def capitalized_name(name: str) -> str:
    """
    Returns a capitalized version of the name.

    Parameters:
    - name (str): The name to be formatted.

    Returns:
    - str: A version of the name with the first letter capitalized.
    """

    return name.capitalize()


def upper_name(name: str) -> str:
    """
    Returns an uppercase version of the name.

    Parameters:
    - name (str): The name to be formatted.

    Returns:
    - str: An uppercase version of the name.
    """

    return name.upper()


def lower_name(name: str) -> str:
    """
    Returns a lowercase version of the name.

    Parameters:
    - name (str): The name to be formatted.

    Returns:
    - str: A lowercase version of the name.
    """

    return name.lower()


def format_number(number: str) -> float:
    """
    Converts a numeric string to a formatted number.

    Removes non-numeric characters from the string and converts it to float.

    Parameters:
    - number (str): The numeric string to be formatted.

    Returns:
    - float: The formatted number.
    """

    # Remove non-numeric characters
    cleaned_number = ''.join([c for c in number if c.isdigit()])

    try:
        # Attempt to convert the cleaned string to float
        formatted_number = float(cleaned_number)
        return formatted_number
    except ValueError:
        # Handle the case where the conversion fails (e.g., if the string is not a valid number)
        raise ValueError(f'Invalid numeric string: {number}')

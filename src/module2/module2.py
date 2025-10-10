"""
EXAMPLE MODULE
DISCARD THIS FOR YOUR PROJECT AND CREATE YOUR OWN MODULES ACCORDING TO YOUR NEEDS

This module provides a 'sum' function to perform addition of two numbers
represented as strings. Before addition, input strings are converted
for numbers formatted using the 'format_number()' function of the 'utils.utils' module.

Author: Filipe de Souza Martins
Date: January 27, 2024
"""

from utils.utils import format_number

from src.logger import logger


def sum_numbers(x: str, y: str) -> float:
    """
    Realiza a soma de dois números representados como strings.

    Converte as strings de entrada para números formatados usando a função
    'format_number()' antes de realizar a soma.

    Parâmetros:
    - x (str): A primeira string que representa o número a ser somado.
    - y (str): A segunda string que representa o número a ser somado.

    Retorna:
    - float: O resultado da soma dos números convertidos.

    Exemplo:
    >> soma('12.34', '56.78')
    69.12
    """

    logger.info(f'Starting print_capitalized_name with name {x} {y}')

    logger.info(f'Converting variables x and y to float')

    x_float = format_number(x)
    y_float = format_number(y)

    result = x_float + y_float

    logger.info(f'Function generated the following result: {result}')

    return result


if __name__ == '__main__':
    print(sum_numbers('R$1.500', 'R$1.500'))
    print(sum_numbers('R$ 1.500', 'R$ 1.500'))
    print(sum_numbers('USD1.500', 'USD 1.500'))
    print(sum_numbers('1.500', 'R$1500'))
    print(sum_numbers('1500', '1500'))

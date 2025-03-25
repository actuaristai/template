"""Start here for scripts."""
from loguru import logger


def add_numbers(first_num: int, second_num: int) -> int:
    """Add two numbers.

    Args:
        first_num (int): first number to add
        second_num (int): second number to add

    Returns:
        int: sum of two numbers

    Examples:
        >>> add_numbers(1, 2)
        3
    """
    add = first_num + second_num
    logger.info('The sum is ' + str(add))
    return add


if __name__ == '__main__':
    add_numbers(1, 2)

"""
Sub module files
"""
def divide(a,b):
    """
    Divide two numbers

    :param a: int or float number
    :param b: int or float number
    :return: c int or float. The quotient of division
    """
    try:
        c = a/b

    except ZeroDivisionError as e:
        c = e
    return c
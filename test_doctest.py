def to_absolute(number):
    """
        Return the absolute value

        :param number: Initial number
        :return:  The absolute value
        >>> to_absolute(3)
        3
        >>> to_absolute(-10)
        10
    """
    if number <= 0:
        return -number
    return number


def to_abss(number):
    if number <= 0:
        return -number
    return number
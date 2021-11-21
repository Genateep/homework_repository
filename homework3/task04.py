def is_armstrong(number: int) -> bool:
    """Returns True if given number is Armstrong number.
    Only positive integers allowed
    """
    return number == sum([int(_)**len(str(number)) for _ in str(number)])

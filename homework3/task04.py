def is_armstrong(number: int) -> bool:
    """Returns True if given number is Armstrong number.
    Only positive integers allowed
    """
    return number == sum([int(i)**len(str(number)) for i in str(number)])

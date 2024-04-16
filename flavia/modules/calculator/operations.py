def square(number:float=None)->float:
    '''
    Squares the provided number
    Example:
        square(5)
        >> 25
    '''
    return number ** 2

def expo(base:float, expo:float) -> float:
    '''
    Gets the base and exponentiates to the expo
    Example:
        expo(5, 3)
        >> 125
    '''
    return base ** expo
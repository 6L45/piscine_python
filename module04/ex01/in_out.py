def square(x: int | float) -> int | float:
    """Returns the square of a given number."""
    return x*x


def pow(x: int | float) -> int | float:
    """Returns the power of a given number to itself."""
    return x**x


def outer(x: int | float, function):
    """
        Returns a function that keeps applying a given function return
        on the result of previous function calls.
    """
    count = 0
    result = None

    def inner():
        """
            Applies a given function return
            on the result of previous function calls.
        """
        nonlocal count, result
        if count == 0:
            result = function(x)
            count += 1
        else:
            result = function(result)
        return result

    return inner

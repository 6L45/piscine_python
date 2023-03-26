from typing import Callable


def callLimit(limit: int) -> Callable:
    """
        A decorator function that takes an integer `limit` as input
        and returns a wrapper function `callLimiter` that
        limits the number of times the decorated function can be called
        to the value of `limit`.
        If the decorated function is called more than `limit` times,
        an error message is printed
        and the function is blocked from further execution.

        Args:
            limit (int):
            The maximum number of times the decorated function can be called.

        Returns:
            Callable:
            The `callLimiter` function that wraps the decorated function.
    """
    count = 0

    def callLimiter(function: Callable) -> Callable:
        """
            A wrapper function returned by the `callLimit`
            decorator that limits the number of times the decorated function
            can be called.

            Args:
                function (Callable): The function to be decorated.

            Returns:
                Callable:
                The `limit_function`
                that wraps the decorated function `function`.
            """

        def limit_function(*args, **kwargs):
            """
                it's in the name...
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: <function {function.__name__} \
at {hex(id(function))}> call too many times")
        return limit_function

    return callLimiter

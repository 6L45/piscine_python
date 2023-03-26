from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Compute and print requested statistics of a sequence of numbers.

    Args:
        args: A variable-length argument list of numbers.
        kwargs: A keyword argument list indicating which statistics to compute.
            Valid keywords are "mean", "median", "quartile", "std", and "var".
            The corresponding values are ignored.

    Returns:
        None.
    """

    required_stats = {"mean", "median", "quartile", "std", "var"}
    requested_stats = set(kwargs.values())
    if not requested_stats <= required_stats:
        print("ERROR")
        return

    n = len(args)
    if n == 0:
        print("ERROR")
        return

    sorted_args = sorted(args)
    mean = sum(args) / n
    median = (sorted_args[n // 2] if n % 2 == 1
              else (sorted_args[n // 2 - 1] + sorted_args[n // 2]) / 2)

    if "mean" in requested_stats:
        print(f"mean : {mean:.1f}")

    if "median" in requested_stats:
        print(f"median : {median:.1f}")

    if "quartile" in requested_stats:
        q1 = sorted_args[n // 4]
        q3 = sorted_args[(3 * n) // 4]
        print(f"quartile : [{q1:.1f}, {q3:.1f}]")

    if "std" in requested_stats:
        variance = sum((x - mean) ** 2 for x in args) / n
        std_deviation = variance ** 0.5
        print(f"std : {std_deviation:.15f}")

    if "var" in requested_stats:
        variance = sum((x - mean) ** 2 for x in args) / n
        print(f"var : {variance:.15f}")

# from tqdm import tqdm
# import time


def ft_tqdm(lst: range) -> None:
    """
        Decorate an iterable with a progress bar.
    """

    total = len(lst)
    for i, item in enumerate(lst, 1):
        advance = int(i * 100 / total)
        remains = 99 - advance
        percentage_str = str(f"{i * 100 / total:.0f}")

        print(percentage_str + "%", end="")
        print(" " * (3 - len(percentage_str)), end="")
        print("|[", end="")
        print("=" * advance, end="")
        print(">" if i != total else "", end="")
        print(" " * remains, end="")
        print("]|", end="")
        print(f" {i}/{total:>2}", end="\r")

        yield item
    print("")

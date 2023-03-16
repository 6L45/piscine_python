import time
from tqdm import tqdm


def ft_tqdm(lst: range) -> None:
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
        print(f"{i}/{total:>2}", end="\r")

        yield item
    print("")


if __name__ == "__main__":
    # example usage
    for _ in ft_tqdm(range(27)):
        time.sleep(0.1)

    for _ in tqdm(range(10)):
        time.sleep(0.1)

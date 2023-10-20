#! /bin/python3

import sys
from ft_filter import ft_filter


def main():
    """
        that's the main function where everything start
    """
    try:
        assert len(sys.argv) == 3
        assert isinstance(sys.argv[1], str)
        assert sys.argv[2][0] != '-'
        assert str(sys.argv[2]).lstrip('-').isdigit()
    except AssertionError:
        print("AssertionError: the arguments are bad")
        exit(1)

    print(ft_filter(lambda x: len(x) > int(sys.argv[2]),
                    sys.argv[1].split()))


if __name__ == "__main__":
    main()

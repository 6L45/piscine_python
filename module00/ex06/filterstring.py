import sys
import ft_filter

if __name__ == "__main__":

    try:
        assert len(sys.argv) == 3
        assert isinstance(sys.argv[1], str)
        assert sys.argv[2][0] != '-'
        assert str(sys.argv[2]).lstrip('-').isdigit()
    except AssertionError:
        print("Usage: python filterstring.py <string> <unsigned integer>")
        exit(1)

    print(ft_filter.ft_filter(lambda x: len(x) == int(sys.argv[2]),
                              sys.argv[1].split()))

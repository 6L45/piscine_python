import sys


def evaluate_str(eval_string):
    """
        evaluate string passed as parameter
        print :
            -total char in string
            -total upper case letter in string
            -total lower case letter in string
            -total punction character in string
            -total space in string
            -total digit character in string
    """

    punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    length = 0
    upper = 0
    lower = 0
    punc = 0
    space = 0
    digit = 0
    for c in eval_string:
        length += 1

        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c in punctuation_marks:
            punc += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
    print("The text contains", length, "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punc, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")


if __name__ == "__main__":

    try:
        assert len(sys.argv) == 2
        string = sys.argv[1]
    except AssertionError:
        string = input("What is the text to count\n")

    evaluate_str(string)

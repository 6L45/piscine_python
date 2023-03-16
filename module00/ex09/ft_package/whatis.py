import sys

if len(sys.argv) < 2:
    exit()

try:
    assert len(sys.argv) == 2
except AssertionError:
    print("AssertionError: more than one argument are provided")
    exit()
try:
    assert str(sys.argv[1]).lstrip('-').isdigit()
    num = int(sys.argv[1])

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError:
    print("AssertionError: argument is not an integer")

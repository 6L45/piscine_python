import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        slice a 2d array according to start and end
        return 2Darray = 2Darray[start:end]
    """

    try:
        arr = np.array(family)
        print(f"My shape is: {arr.shape}")

        arr = arr[start:end]
        print(f"My new shape is: {arr.shape}")

        return arr.tolist()

    except TypeError:
        print("Error: Input list must be a 2D array")
        exit(1)

    except IndexError:
        print("Error: Start or end indices out of bounds")
        exit(1)


# SLICING EXEMPLE
# array [
#         [10, 11, 12, 13, 14, 15]
#         [20, 21, 22, 23, 24, 25]
#         [30, 31, 32, 33, 34, 35]
#         [40, 41, 42, 43, 44, 45]
#         [50, 51, 52, 53, 54, 55]
#                                  ]

# [:, 2:4] <-- from all row ( 1rst dimension [ ...   <--- first [
#                                              ...
#                                              ...
#                                              ...
#                                              ...
#                                                  ] ) <-- to last ]
#
#                                                   only one dimension here
#                                              but if several first slice level


# [:, 2:4] <-- 2:4 from index 2 to index 4 excluded so index 3 at 2nd lvl:
#
#   [10, 11, 12, 13, 14, 15] -> index 2 to 4(excluded) = [12, 13]

# so result of arr slicing [:, 2:4]
#        [
#         [12, 13]
#         [22, 23]
#         [32, 33]
#         [42, 43]
#         [52, 53]
#                 ]

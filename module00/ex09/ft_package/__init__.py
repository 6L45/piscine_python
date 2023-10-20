def count_in_list(lst, val) -> int:
    """
        count_in_list(lst, val) -> int
        count and return number of val in lst
    """
    return sum(1 for x in lst if x == val)

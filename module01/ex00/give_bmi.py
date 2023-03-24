import numpy as np


class SizeError(Exception):
    pass


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        apply_limit(arr, limit)
        return an array from arr with only the values above limit
    """

    bmi_arr = np.array(bmi)
    bool_arr = bmi_arr > limit
    return bool_arr.tolist()


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
       return a list of Body Mass Index
       built from the 2 lists passed as parameters
    """

    if not isinstance(height, list):
        raise TypeError("height is not a list")

    if not isinstance(weight, list):
        raise TypeError("weight is not a list")

    height_arr = np.array(height)
    weight_arr = np.array(weight)

    # CHECK IF HEIGHT AND WEIGHT GOT THE SAME LENGTH
    if height_arr.shape != weight_arr.shape:
        raise SizeError("different size for height_arr and weight_arr")

    # IF LEN == 0 RETURN EMPTY LIST
    if height_arr.size == 0:
        return height

    # CHECK IF HEIGHT OR WEIGHT CONTAIN ANY VALUE OTHER THAN INT OR FLOAT
    if not np.issubdtype(height_arr.dtype, np.number):
        raise TypeError("element in height_arr different than int or float")

    if not np.issubdtype(weight_arr.dtype, np.number):
        raise TypeError("element in weight_arr different than int or float")

    # CALCULATE BMI
    bmi = weight_arr / (height_arr ** 2)

    return bmi.tolist()

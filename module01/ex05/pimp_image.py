#! /bin/python3

import numpy as np
from PIL import Image
from load_image import ft_load
from matplotlib import pyplot as plt


def display(img):
    if img.size > 0:
        try:
            plt.imshow(Image.fromarray(img))
            plt.show()
        except ValueError:
            print("Et non gaston!")
            exit(1)


def ft_invert(img_array) -> np.array:
    """
        Invert the colors of the image received.
    """

    new_array = img_array.copy()
    new_array = 255 - new_array
    display(new_array)

    return (new_array)


def ft_red(img_array) -> np.array:
    """
        Apply a red tone filter to an image
    """

    new_array = img_array.copy()
    new_array[:, :, 1] = 0  # Set the green channel to 0
    new_array[:, :, 2] = 0  # Set the blue channel to 0
    display(new_array)

    return (new_array)


def ft_blue(img_array) -> np.array:
    """
        Apply a blue tone filter to an image
    """

    new_array = img_array.copy()
    new_array[:, :, 0] = 0  # Set the red channel to 0
    new_array[:, :, 1] = 0  # Set the green channel to 0
    display(new_array)

    return (new_array)


def ft_green(img_array) -> np.array:
    """
    Apply a green tone filter to an image
    """

    new_array = img_array.copy()
    new_array[:, :, 0] = 0  # Set the red channel to 0
    new_array[:, :, 2] = 0  # Set the blue channel to 0
    display(new_array)

    return (new_array)


def ft_grey(img_array) -> np.array:
    """
    Convert an image to ft_grey
    """

    new_array = img_array.copy()
    new_array = np.dot(new_array[..., :3], [0.2989, 0.5870, 0.1140])
    display(new_array)

    return (new_array)


def main():
    """
        that s the main
    """
    try:
        src = input("please select an image\n")
        if src == "quit":
            exit(0)
        if not src:
            src = "landscape.jpg"

        img_data = ft_load(src)

        user_input = ""
        while 1:
            user_input = input("<red>(r) <green>(g) <blue>(b) \
<gray>(gs) <invert>(i)\n")
            if user_input == "quit":
                exit(0)
            if not user_input:
                print("please select a filter")
                print("<red>(r) <green>(g) <blue>(b) <gray>(gs) <invert>(i)")
            elif len(user_input.split(" ")) > 1:
                print("too many arguments")
            elif user_input not in ["red", "r", "green", "g", "blue", "b",
                                    "gray", "gs", "invert", "i"]:
                print("bad arguments")
            else:
                if user_input == "red" or user_input == "r":
                    ft_red(img_data)

                if user_input == "green" or user_input == "g":
                    ft_green(img_data)

                if user_input == "blue" or user_input == "b":
                    ft_blue(img_data)

                if user_input == "gray" or user_input == "gs":
                    ft_grey(img_data)

                if user_input == "invert" or user_input == "i":
                    ft_invert(img_data)

    except (KeyboardInterrupt, EOFError):
        print("\rquit")
    except ValueError:
        print("Et non gaston!")
        exit()


if __name__ == "__main__":
    main()

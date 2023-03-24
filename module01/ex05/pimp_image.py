import numpy as np
from PIL import Image
from load_image import ft_load
from matplotlib import pyplot as plt


def invert_colors(img_array):
    """
        Invert the colors of an image
    """

    return 255 - img_array


def red_tone(img_array):
    """
        Apply a red tone filter to an image
    """

    new_array = img_array.copy()
    new_array[:, :, 1] = 0  # Set the green channel to 0
    new_array[:, :, 2] = 0  # Set the blue channel to 0
    return new_array


def blue_tone(img_array):
    """
        Apply a blue tone filter to an image
    """

    new_array = img_array.copy()
    new_array[:, :, 0] = 0  # Set the red channel to 0
    new_array[:, :, 1] = 0  # Set the green channel to 0
    return new_array


def green_tone(img_array):
    """
    Apply a green tone filter to an image
    """

    new_array = img_array.copy()
    new_array[:, :, 0] = 0  # Set the red channel to 0
    new_array[:, :, 2] = 0  # Set the blue channel to 0
    return new_array


def grayscale(img_array):
    """
    Convert an image to grayscale
    """

    return np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140])


if __name__ == "__main__":

    try:
        src = input("please select an image\n")
        if src == "quit":
            exit()
        if not src:
            src = "landscape.jpg"

        img_data = ft_load(src)

        user_input = ""
        while 1:
            user_input = input("<red> <green> <blue> <gray> <invert>\n")
            if user_input == "quit":
                print("\rquit")
                exit()
            if not user_input:
                print("please select a filter")
                print("<red> <green> <blue> <gray> <invert>")
            elif len(user_input.split(" ")) > 1:
                print("too many arguments")
            elif user_input not in ["red", "r", "green", "g", "blue", "b",
                                    "gray", "gs", "invert", "i"]:
                print("bad arguments")
            else:
                img = np.empty_like(img_data)
                if user_input == "red" or user_input == "r":
                    img = red_tone(img_data)

                if user_input == "green" or user_input == "g":
                    img = green_tone(img_data)

                if user_input == "blue" or user_input == "b":
                    img = blue_tone(img_data)

                if user_input == "gray" or user_input == "gs":
                    img = grayscale(img_data)

                if user_input == "invert" or user_input == "i":
                    img = invert_colors(img_data)

                if img.size > 0:
                    plt.imshow(Image.fromarray(img))
                    plt.show()

    except (KeyboardInterrupt, EOFError):
        print("\rquit")
    except ValueError:
        print("Et non gaston!")
        exit()

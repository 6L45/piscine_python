from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
        open image at path given as parameter
        and return pixel data of the image
    """

    try:
        # Load image and convert to RGB format
        # with close automatically when finished
        with Image.open(path).convert("RGB") as img:

            print(f"The shape of image is: \
{img.size[1]}, {img.size[0]}, {len(img.mode)}")

            pixel_data = np.array(img)

            return pixel_data

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        exit(1)

    except ValueError as e:
        print(f"Error: Could not load image at '{path}': {e}")
        exit(1)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)

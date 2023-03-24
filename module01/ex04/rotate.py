from matplotlib import pyplot as plt
from PIL import Image
from load_image import ft_load


def zoom(img_array, x1, y1, x2, y2, filename, direct):
    """
        create from img_data a new cut image according to the values given
    """
    sliced_array = img_array[x1:x2, y1:y2]

    # Convert the slice to a PIL Image object
    sliced_image = Image.fromarray(sliced_array)
    sliced_image = sliced_image.rotate(90 * direct)
    print(f"The new shape rotated image is: \
{sliced_image.size[1]}, {sliced_image.size[0]}")

    print("(height =", sliced_image.size[1], end=" ")
    print("| width =", sliced_image.size[0], end=")\n")
    # Save the image to a file
    sliced_image.save(filename)

    plt.imshow(sliced_image)
    plt.show()


if __name__ == "__main__":

    y2 = 400
    x2 = 400
    y1 = 0
    x1 = 0
    path = "zoomed.jpeg"

    try:
        src = input("please select an image\n")
        if src == "quit":
            exit()
        if src == path:
            print("dest file smells like inception")
            exit()
        if not src:
            src = "animal.jpeg"

        img_data = ft_load(src)

        height, width, channel = img_data.shape
        print()
        print("height =", height, end=" ")
        print("| width =", width, end="\n")

        print("\nif animal.jpeg -> subject ~= 400 900 100 500")
        print(f"please enter: <x1> <x2> max {width - 1} \
/ <y1> <y2> max {height - 1} / <direction> (right or left)")
        print("or enter dflt for default values")
        user_input = ""
        direct = 0
        while True:

            user_input = input()
            err = False

            if user_input:
                if user_input == "quit":
                    exit()

                if user_input == "dflt":

                    x1 = int(width / 3)
                    y1 = int(height / 3)
                    x2 = int(x1 * 2)
                    y2 = int(y1 * 2)
                    direct = -1
                    zoom(img_data, y1, x1, y2, x2, path, direct)

                else:
                    user_input_list = user_input.split(" ")

                    if len(user_input_list) != 5:
                        print("bad arguments")

                    else:
                        x1 = int(user_input_list[0].strip())
                        x2 = int(user_input_list[1].strip())
                        y1 = int(user_input_list[2].strip())
                        y2 = int(user_input_list[3].strip())

                        if user_input_list[4].strip() == "left":
                            direct = 1
                        elif user_input_list[4].strip() == "right":
                            direct = -1
                        elif user_input_list[4].strip() == "null":
                            direct = 0
                        else:
                            print("ErrorValue: direction = right or left")
                            err = True

                        if y2 <= y1 or y2 < 0 or y1 < 0:
                            print(f"ErrorValue: y1({y1}) / y2({y2}): \
y2 <= y1 or y2 <= 0 or y1 <= 0")
                            err = True
                        if y1 >= height or y2 >= height:
                            print(f"ErrorValue: max height = {height}: \
y1({y1}) /  y2({y2})")
                            err = True

                        if x2 <= x1 or y2 < 0 or y1 < 0:
                            print(f"ErrorValue: x1({x1}) / x2({x2}): \
x2 <= x1 or x2 <= 0 or x1 <= 0")
                            err = True
                        if x1 >= width or x2 >= width:
                            print(f"ErrorValue: max width = {width}: \
x1({x1}) / x2({x2})")
                            err = True

                        if not err:
                            zoom(img_data, y1, x1, y2, x2, path, direct)

                print(f"\nplease enter: <x1> <x2> max {width - 1} \
/ <y1> <y2> max {height - 1} / <direction> (right or left)")
                print("or enter dflt for default values")

    except (KeyboardInterrupt, EOFError):
        print("\rquit")
    except ValueError:
        print("out of range or bs entry")
        exit()

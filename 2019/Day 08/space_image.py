"""Day 08 Answers"""
from itertools import dropwhile


def decode_layers(digits: list, width=25, height=6):
    """Each image actually consists of a series of identically-sized layers that are filled in this way. So, the first digit corresponds to the top-left pixel of the first layer, the second digit corresponds to the pixel to the right of that on the same layer, and so on until the last digit, which corresponds to the bottom-right pixel of the last layer.
    The image you received is 25 pixels wide and 6 pixels tall."""

    img_size = width * height
    n_layers, reminder = divmod(len(digits), img_size)
    assert reminder == 0
    layers = [digits[num * img_size : (num + 1) * img_size] for num in range(n_layers)]
    return layers


def decode_pixel(candidates):
    """The digits indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is transparent."""
    candidates = dropwhile(lambda x: x == 2, candidates)
    color = next(candidates)
    assert color is not None
    return color


def decode_image(layers: list, width=25, height=6):
    """The image is rendered by stacking the layers and aligning the pixels with the same positions in each layer. The digits indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is transparent.

    The layers are rendered with the first layer in front and the last layer in back. So, if a given position has a transparent pixel in the first and second layers, a black pixel in the third layer, and a white pixel in the fourth layer, the final image would have a black pixel at that position."""

    stack = zip(*layers)
    image = []
    for _ in range(height):
        row = "".join(" #"[decode_pixel(next(stack))] for y in range(width))
        image.append(row)
    return "\n".join(image)


INPUT = "2019/Day 08/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        digits = list(map(int, data.read().strip()))
    layers = decode_layers(digits)
    layer = min(layers, key=lambda l: l.count(0))
    return layer.count(1) * layer.count(2)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        digits = list(map(int, data.read().strip()))
    layers = decode_layers(digits)
    image = decode_image(layers)
    return image


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2:\n{ANSWER2}")

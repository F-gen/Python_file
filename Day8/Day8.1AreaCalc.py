import math

test_h = int(input("Height of wall"))
test_w = int(input("width of wall"))
coverage = 5


def print_calc(height, width, cover):
    print(math.ceil((width * height) / cover))


print_calc(height=test_h, width=test_w, cover=coverage)

import math
def polygon_area(sides, length):
    """ Calculates the area of a polygon """
    area = (sides * length ** 2) / (4 * (math.tan(math.pi/sides)))
    return area

print(polygon_area(7, 3))
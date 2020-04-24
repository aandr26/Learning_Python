
def is_mary(x):
    if x == "Mary":
        print ("Found Mary!")
    else:
        print ("No Mary")

is_mary("Mary")
is_mary("Mark")

import math

def area_triangle_sss(side1, side2, side3):
    """
    Returns the area of a triangle given the lengths of
    its three sides.
    """
    # Heron's formula
    semi_perim = (side1 + side2 + side3) / 2.0
    return math.sqrt(semi_perim*
                     (semi_perim-side1) * 
                     (semi_perim-side2) *
                     (semi_perim-side3))


def favorites(instructor):
    """Returns the favorite thing of the given instructor."""
    if instructor == "Joe":
        return "games"
    elif instructor == "Scott":
        return "ties"
    elif instructor == "John":
        return "outdoors"
    else:
        print ("favorites saw invalid instructor: " + instructor)

favorites("Joe")
favorites("Aaron")
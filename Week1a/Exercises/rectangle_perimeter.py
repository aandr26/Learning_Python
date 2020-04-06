# Get the area of the triangle from width and height
def rectangle_perimeter(width,height):
    perimeter = width*2 + height*2
    return perimeter

# Test
def test(width,height):
    print("A rectangle " + str(width) + " inches wide and " + str(height),)
    print("inches high has a perimeter of",)
    print(str(rectangle_perimeter(width,height)) + " inches.")

test(4,7)
test(7,4)
test(10,10)


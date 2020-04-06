import math
# Calculate the area of a triangle
def triangle_area(x0,y0,x1,y1,x2,y2):
    sidea = math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
    sideb = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    sidec = math.sqrt((x0 - x2)**2 + (y0 - y2)**2)
    thesemi = .5*(sidea+sideb+sidec)
    area = math.sqrt(thesemi*(thesemi - sidea)*(thesemi - sideb)*(thesemi - sidec))
    print (area)
    return area

triangle_area(0, 0, 3, 4, 1, 1)
triangle_area(-2, 4, 1, 6, 2, 1)
triangle_area(10, 0, 0, 0, 0, 10)
